HEADERS = $(wildcard */*.h) $(wildcard native/*/*.h)
OBJECTS = $(patsubst %.c, %.o, $(wildcard *.c)) $(patsubst %.c, %.o, $(wildcard */*.c)) $(patsubst %.c, %.o, $(wildcard native/*/*.c))

default: program

%.o: %.c $(HEADERS)
	@gcc -c $< -o $@

program: $(OBJECTS)
	@gcc $(OBJECTS) -o $@

clean:
	@-rm -f $(OBJECTS)
	@-rm -f program
