#include <iostream>
#include <isa-l/crc.h>

int main(void) {
    isal_version_info_data* id = isal_version_info(ISALVERSION_NOW);
    if (!id) {
        return 1;
    }
    std::cout << "protocols: ";
    for(auto proto = id->protocols; *proto; proto++) {
        std::cout << *proto;
    }
    std::cout   << "\nversion: "        << id->version
                << "\nssl version: "    << id->ssl_version
                << "\nfeatures: "       << id->features
                << "\n";

    if ( crc16_t10dif(0x8005, "32311E333530", 12) == 0xb4c9 ) {
        std::cout << "Succeed\n";
    } else {
        std::cout << "Failed to init isal\n";
        retval = 3;
    }
    return retval;
}
