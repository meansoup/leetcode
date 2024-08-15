bool lemonadeChange(int* bills, int billsSize) {
    int d5 = 0;
    int d10 = 0;
    
    for (int i = 0; i < billsSize; i++) {
        if (bills[i] == 5) {
            d5 += 1;
        } else if (bills[i] == 10) {
            if (d5 == 0) {
                return false;
            }
            d5 -= 1;
            d10 += 1;
        } else {
            if (d10 > 0 && d5 > 0) {
                d5 -= 1;
                d10 -= 1;
            } else if (d10 == 0 && d5 > 2) {
                d5 -= 3;
            } else {
                return false;
            }
        }
    }
    
    return true;
}