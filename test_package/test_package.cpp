#include <iostream>
#include <isa-l/crc.h>

int main(void) {
    if ( crc16_t10dif(0x8005, "32311E333530", 12) != 0xb4c9 ) {
        std::cout << "Failed to install ISA-L\n";
        return -1;
    }
    std::cout << "Success\n";
    return 0;
}
