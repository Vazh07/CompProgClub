# Compiler
CC = g++

# lib path
LIB_PATH = ../../FileReader/

# Compiler flags
CFLAGS = -Wall -Wextra -std=c++11 -I $(LIB_PATH)
LDFLAGS = -L $(LIB_PATH)

# Directory containing source files
SRC_DIR = src

# Directory containing object files
OBJ_DIR = obj

# Directory containing header files
INC_DIR = include

# Source files
SRCS = $(wildcard $(SRC_DIR)/*.cpp)

# Object files
OBJS = $(patsubst $(SRC_DIR)/%.cpp,$(OBJ_DIR)/%.o,$(SRCS))

# Executable name
EXEC = solution

#Library name
LIB_NAME = fileReader

# Static library name
STATIC_LIB = $(LIB_NAME).a

# Dynamic library name
DYNAMIC_LIB = $(LIB_NAME).so

# Default target
all: $(EXEC)

# Linking the executable dynamically
$(EXEC)_dynamic: $(OBJS) $(DYNAMIC_LIB)
	$(CC) $(CFLAGS) -o $(EXEC) $(OBJS)
#//g++ sol.cpp -o solution -I ../../../FileReader/ -L ../../../FileReader/ -l:libFileReader.a
# Linking the executable statically
$(EXEC)_static: $(OBJS) $(STATIC_LIB)
	$(CC) $(CFLAGS) -o $(EXEC) $(OBJS)

# Compiling source files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp | $(OBJ_DIR)
	$(CC) $(CFLAGS) -I$(INC_DIR) -c $< -o $@

# Creating the object directory
$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

# Creating the dynamic library
$(DYNAMIC_LIB): $(OBJS)
	$(CC) -shared -o $@ $(OBJS)

# Creating the static library
$(STATIC_LIB): $(OBJS)
	ar rcs $@ $(OBJS)

# Phony target to clean object files and executables
.PHONY: clean
clean:
	rm -rf $(OBJ_DIR) $(EXEC) $(STATIC_LIB) $(DYNAMIC_LIB)

# Phony target to run the dynamically linked executable
.PHONY: run_dynamic
run_dynamic: $(EXEC)_dynamic
	./$(EXEC)

# Phony target to run the statically linked executable
.PHONY: run_static
run_static: $(EXEC)_static
	./$(EXEC)

# Phony target to rebuild
.PHONY: rebuild
rebuild: clean all

# Phony target to rebuild dynamically linked executable
.PHONY: rebuild_dynamic
rebuild_dynamic: clean $(EXEC)_dynamic

# Phony target to rebuild statically linked executable
.PHONY: rebuild_static
rebuild_static: clean $(EXEC)_static
