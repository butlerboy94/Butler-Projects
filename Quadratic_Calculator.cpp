#include <iostream>
#include <string>
#include <sstream>
#include <numeric>   // std::gcd
#include <cmath>
#include <cstdlib>
using namespace std;

using i64 = long long;

// integer sqrt floor
i64 isqrt(i64 n) {
    if (n <= 0) return 0;
    return static_cast<i64>(floor(sqrt(static_cast<long double>(n))));
}

// make denominator positive; move sign to numerator
void normalize_sign(i64 &num, i64 &den) {
    if (den < 0) { num = -num; den = -den; }
}

// reduce num/den by gcd
void reduce(i64 &num, i64 &den) {
    if (den == 0) return;
    normalize_sign(num, den);
    i64 g = std::gcd(num < 0 ? -num : num, den);
    if (g) { num /= g; den /= g; }
}

// print a reduced fraction
void print_frac(i64 num, i64 den) {
    reduce(num, den);
    if (den == 1) cout << num;
    else cout << num << "/" << den;
}

// factor out maximal square: n = k^2 * d', with d' squarefree
void extract_square_part(i64 n, i64 &k, i64 &dprime) {
    k = 1; dprime = n;
    for (i64 p = 2; p * p <= dprime; ++p) {
        i64 cnt = 0;
        while (dprime % p == 0) { dprime /= p; ++cnt; }
        if (cnt >= 2) {
            i64 pairs = cnt / 2;
            while (pairs--) k *= p;
            // leftover factor p if cnt odd is already in dprime
        }
    }
    // if dprime==1, fine; if prime > sqrt(original), left as is
}

// try to divide all terms by a common integer factor h
// (-B ± k√d') / (2A)  ==> divide B, k, 2A by h if h | B, h | k, h | 2A
void divide_common(i64 &B, i64 &k, i64 &twoA) {
    i64 h = std::gcd(std::gcd(llabs(B), llabs(k)), llabs(twoA));
    if (h > 1) {
        B   /= h;
        k   /= h;
        twoA/= h;
    }
    normalize_sign(B, twoA); // keep denominator positive
}

// print form: (x = ( -B ± k√d' ) / twoA)
// if d'==1 omit √1; if k==0 omit radical completely (won't happen here)
void print_symbolic_pair(i64 B, i64 k, i64 dprime, i64 twoA, bool complex_imag=false) {
    auto print_one = [&](int sign){ // sign = +1 or -1 for ±
        cout << "(x = ";
        // numerator: -B ± (i?) k√d'
        i64 num_const = -B;
        bool has_const = (num_const != 0);
        bool has_rad   = (k != 0);

        // print constant part if any
        if (has_const) cout << num_const;

        if (has_rad) {
            // print separator with correct sign and spacing
            if (has_const) cout << (sign >= 0 ? " + " : " - ");
            else if (sign < 0) cout << "-";

            if (complex_imag) cout << "i";

            if (llabs(k) != 1 || dprime == 1) cout << llabs(k);

            if (dprime != 1) {
                if (llabs(k) != 1 || complex_imag) cout << "√" << dprime;
                else cout << "√" << dprime; // k == ±1 => just √d'
            }
        }

        cout << ")/";
        cout << twoA << ")";
    };

    // ensure denominator positive
    if (twoA < 0) { B = -B; twoA = -twoA; }

    print_one(+1);
    print_one(-1);
    cout << "\n";
}

int main() {
    i64 A, B, C;

    cout << "Enter A, B, C (e.g., 2 3 -2 or 2, 3, -2): ";
    string line; getline(cin, line);
    if (line.empty()) getline(cin, line);
    for (char &ch : line) if (ch == ',') ch = ' ';
    istringstream iss(line);
    if (!(iss >> A >> B >> C)) {
        cerr << "Invalid input.\n";
        return 1;
    }

    // linear / degenerate cases
    if (A == 0) {
        if (B == 0) {
            cout << ((C == 0) ? "(infinitely many solutions)\n" : "(no solution)\n");
        } else {
            // x = -C/B
            cout << "(x = ";
            print_frac(-C, B);
            cout << ")\n";
        }
        return 0;
    }

    i64 twoA = 2 * A;
    i64 D = B*B - 4*A*C;

    if (D == 0) {
        // one repeated rational root: x = -B/(2A)
        cout << "(x = ";
        print_frac(-B, twoA);
        cout << ")(x = ";
        print_frac(-B, twoA);
        cout << ")\n";
        return 0;
    }

    if (D > 0) {
        i64 r = isqrt(D);
        if (r * r == D) {
            // perfect square -> exact rational fractions
            cout << "(x = ";
            print_frac(-B + r, twoA);
            cout << ")(x = ";
            print_frac(-B - r, twoA);
            cout << ")\n";
        } else {
            // irrational real roots: pull squares out, reduce common factor
            i64 k, dprime; extract_square_part(D, k, dprime); // D = k^2 * dprime
            // divide common factor among B, k, 2A
            divide_common(B, k, twoA);
            print_symbolic_pair(B, k, dprime, twoA, /*complex_imag=*/false);
        }
    } else { // D < 0 : complex roots
        i64 Dabs = -D;
        i64 r = isqrt(Dabs);
        i64 k, dprime; 
        if (r * r == Dabs) { // perfect square imaginary part
            k = r; dprime = 1;
        } else {
            extract_square_part(Dabs, k, dprime); // Dabs = k^2 * dprime
        }
        divide_common(B, k, twoA);
        print_symbolic_pair(B, k, dprime, twoA, /*complex_imag=*/true);
    }
    return 0;
}

