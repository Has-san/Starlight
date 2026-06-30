// ArduinoTwitchBot
// Sample code required to make the bot work on the Arduino side - this is just as example, you can use the incoming signals however you want!
// Schematic provided in respective repo.
// For more info, visit: https://github.com/Stukeley/ArduinoTwitchBot

// Pins.
#define RED_PIN 11
#define GREEN_PIN 9
#define BLUE_PIN 10

#define SIZE_MAX_BUFFER 64
#define SIZE_MAX_COMMAND 16

// Alert mesages (note - they can also be of type int or byte).
// IMPORTANT: these commands here must match the commands in ArduinoTwitchBot app.
String commandTurnOn = "ON";
String commandTurnOff = "OFF";
String commandBlink = "BLINK";
//String commandVary = "VARY";

struct Color {
  int red;
  int green;
  int blue;
  String name;
};

struct Color red = { 255, 0, 0, "RED" };
struct Color green = { 0, 255, 0, "GREEN" };
struct Color blue = { 0, 0, 255, "BLUE" };
struct Color yellow = { 255, 255, 0, "YELLOW" };
struct Color orange = { 244, 102, 27, "ORANGE" };
struct Color cyan = { 0, 255, 255, "CYAN" };
struct Color purple = { 93, 18, 53, "PURPLE" };  //5D1235
struct Color pink = { 253, 108, 158, "PINK" };
struct Color white = { 255, 255, 255, "WHITE" };
struct Color noColor = { 0, 0, 0, "NO COLOR" };
struct Color previousColor = noColor;

void setup() {
  // Setup pins.
  Serial.println("Setup Pins");
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  initColor();
  // Setup Serial.
  Serial.begin(9600);
  Serial.println("Ready !");
}

void loop() {

  String command;

  // If we can read from Serial.
  if (Serial.available() > 0) {
    int commandRed = 0;
    int commandGreen = 0;
    int commandBlue = 0;
    int commandNbBlinks = 0;

    String command = readCommand();

    /*if (command != commandTurnOff){
        commandRed = Serial.readStringUntil(' ').toInt();
        commandGreen = Serial.readStringUntil(' ').toInt();
        commandBlue = Serial.readStringUntil(' ').toInt();
        if (command == commandBlink) commandNbBlinks = Serial.readStringUntil(' ').toInt();
      }*/

    // Display the command.
    /*Serial.println("Red: " + commandRed); 
      Serial.println("Green: " + commandGreen); 
      Serial.println("Blue: " + commandBlue); 
      Serial.println("Blink: " + commandNbBlinks); */
    handleCommand(command);
  }
}

void initColor() {
  setColor(red);
  delay(50);
  setColor(green);
  delay(50);
  setColor(blue);
  delay(50);
  setColor(yellow);
  delay(50);
  setColor(orange);
  delay(50);
  setColor(cyan);
  delay(50);
  setColor(purple);
  delay(50);
  setColor(pink);
  delay(50);
  setColor(white);
  delay(50);
  setColor(noColor);
}

void setColor(Color color) {
  analogWrite(RED_PIN, color.red);
  analogWrite(GREEN_PIN, color.green);
  analogWrite(BLUE_PIN, color.blue);
}

void blinkLed(Color color, int duration, int times) {
  for (int i = 0; i < times; i++) {
    setColor(color);
    delay(duration);
    setColor(noColor);
    delay(duration);
  }
  setColor(previousColor);
}

String readCommand() {
  String command = Serial.readStringUntil('\n');
  command.trim();  //Enlève les parasites
  Serial.println("readCommand() : " + command);
  return command;
}

void handleCommand(String message) {  // Turn the respective LED on based on what the content of the command was.

  char buffer[SIZE_MAX_BUFFER], command[SIZE_MAX_COMMAND], color[SIZE_MAX_COMMAND];
  buffer[0] = '\0';
  command[0] = '\0';
  color[0] = '\0';

  Color colorSelected, currentColor;
  int nbBlinks = 0, duration = 0;

  strncpy(buffer, message.c_str(), SIZE_MAX_BUFFER - 1);

  int parsed = sscanf(buffer, "%15s %15s %d %d", command, color, &nbBlinks, &duration);
  
  colorSelected = selectColor(color);

  Serial.println("handleCommand() : Previous color was " + previousColor.name + ".");
  if (strcmp(command, commandTurnOff.c_str()) == 0) {
    //Serial.println("Command Turn OFF");
    setColor(noColor);
    saveData(noColor);
  } 
  
  else if (strcmp(command, commandTurnOn.c_str()) == 0) {
    if (parsed < 2)
      logError("handleCommand() : No color selected");
    else {
      Color selectedColor = selectColor(color);
      Serial.println("handleCommand() : selected color : " + selectedColor.name + ".");
      setColor(selectedColor);
      saveData(selectedColor);
    }
  } 
  
  else if (strcmp(command, commandBlink.c_str()) == 0) {
    Serial.print("Command BLINK ");
    if (parsed < 2)
      logError("handleCommand() : No color selected");
    else if (parsed < 3 || nbBlinks == 0)
      logError("handleCommand() : No blinks requested");
    else if (parsed < 4 || duration == 0)
      logError("handleCommand() : No duration requested");
    else {
      /*Serial.print(color);
      Serial.print(" ");
      Serial.print(nbBlinks);
      Serial.print(" times ");
      Serial.print(duration);
      Serial.print(" ms.");*/
      blinkLed(colorSelected, duration, nbBlinks);
    }
  } 
  
  else {
    logError(strcat("handleCommand() : not a configured command : ", command));
  }
}

Color selectColor(String command) {
  Color color;
  //Serial.println("selectColor : " + command + ".");
  //Serial.println("previousColor : " + previousColor.name + ".");
  if (command == "RED") color = red;
  else if (command == "GREEN") color = green;
  else if (command == "BLUE") color = blue;
  else if (command == "YELLOW") color = yellow;
  else if (command == "ORANGE") color = orange;
  else if (command == "CYAN") color = cyan;
  else if (command == "PURPLE") color = purple;  //5D1235
  else if (command == "PINK") color = pink;
  else if (command == "WHITE") color = white;
  else {
    Serial.println("SelectColor() : Previous color was " + previousColor.name + ".");
    //color = previousColor;
    logError("SelectColor() : '" + command + "'" + " unknown.");
  }
  return color;
}

void logError(String errorMessage) {
  Serial.println(errorMessage);
}

void saveData(Color data) {
  Serial.println("saveData() : Previous color was " + previousColor.name + ".");
  Serial.println("saveData() : new color was " + data.name + ".");
  previousColor = data;  
  Serial.println("saveData() : Previous color is now  " + previousColor.name + ".");
}
