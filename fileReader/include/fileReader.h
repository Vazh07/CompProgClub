//A small gizmo that reads and returns the data of each line of a file as an array of strings
// fileReader.h
#ifndef FILEREADER_H
#define FILEREADER_H

#include <string>
#include <vector>

// Function declaration
std::vector<std::string> readFromFile(const std::string& filename);
std::vector<std::string> splitString(const std::string& str, char delimiter);
#endif // FILEREADER_H
