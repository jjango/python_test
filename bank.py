 if (index === line.length && lineNum < (lines.length-1)) {
lineNum++;
line = lines[lineNum];
do {
  lineNum++;
  line = lines[lineNum];
} while (line.length === 0);
   DEBUG && debug(line); // jshint ignore:line
   index = 0;
 }
