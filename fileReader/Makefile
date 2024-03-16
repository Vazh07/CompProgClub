# Compiler
CC = g++
AR = ar
RCS = rcs
# Compiler flags
CFLAGS = -Wall -Wextra -std=c++11 -I $(LIB_PATH)

# src path
SRC_PATH = src/
# obj path
OBJ_PATH = obj/
# lib path
LIB_PATH = lib/

# Compiler flags
CFLAGS = -Wall -Wextra -std=c++11 -I $(LIB_PATH)

#Library name
LIB_NAME = fileReader
# Static library name
STATIC_LIB = lib$(LIB_NAME).a
# Dynamic library name
DYNAMIC_LIB = lib$(LIB_NAME).so

# Building dynamic lib
dynamic:
	$(CC) -c -fPIC $(SRC_PATH)$(LIB_NAME).cpp -o $(OBJ_PATH)$(LIB_NAME).o
	$(CC) -shared -o $(LIB_PATH)$(DYNAMIC_LIB) $(OBJ_PATH)$(LIB_NAME).o

# Building static lib
static:
	$(CC) -c $(SRC_PATH)$(LIB_NAME).cpp -o $(OBJ_PATH)$(LIB_NAME).o
	ar rcs $(LIB_PATH)$(STATIC_LIB) $(OBJ_PATH)$(LIB_NAME).o


#g++ -c src/fileReader.cpp -o obj/fileReader.o
#ar rcs lib/libFileReader.a obj/fileReader.o
#g++ -c -fPIC src/fileReader.cpp -o obj/fileReader.o
#g++ -shared -o lib/libFileReader.so obj/fileReader.o

# Phony target to clean object files and executables
.PHONY: clean
clean:
	rm -rf $(OBJ_PATH)
	rm -rf $(LIB_PATH)
	mkdir obj
	mkdir lib

# Phony target to rebuild
.PHONY: rebuild
rebuild: clean all

# Phony target to rebuild dynamically linked executable
.PHONY: rebuild_dynamic
rebuild_dynamic: clean dynamic

# Phony target to rebuild statically linked executable
.PHONY: rebuild_static
rebuild_static: clean static
