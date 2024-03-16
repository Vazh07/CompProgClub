// fileReader.cpp
#include "../include/fileReader.h"
#include <fstream>
#include <sstream>
#include <vector>

/*std::string readFromFile(const std::string& filename) {
    std::ifstream file(filename);
    std::stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}*/

std::vector<std::string> splitString(const std::string& str, char delimiter) {
    std::vector<std::string> tokens;
    std::istringstream iss(str);
    std::string token;

    while (std::getline(iss, token, delimiter)) {
        tokens.push_back(token);
    }

    return tokens;
}


std::vector<std::string> readFromFile(const std::string& filename) {
    std::ifstream file(filename);
    std::vector<std::string> lines; // Vector to store lines

    if (!file.is_open()) {
        // Handle file opening failure
        //std::cerr << "Error: Could not open file " << filename << std::endl;
        return lines; // Return empty vector
    }

    std::string line;
    while (std::getline(file, line)) {
        lines.push_back(line); // Add line to vector
    }

    return lines; // Return vector containing lines
}
