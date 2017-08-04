
#include <sstream>
#include <string>
#include "../src/tstream.h"

int main(int argc, char **argv) {
	tstream::server ser("127.0.0.1", 5333);
	ser.listen();
	auto con = ser.accept();
	char line[1024];
	while (!con.eof()) {
		char c;
		//con >> c; cout << c;
		con.getline(line, 1024);
		cout << line << endl;
	}
	return 0;
}