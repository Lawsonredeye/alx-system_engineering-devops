# 0x04. Loops, conditions and parsing

Bash has always been used for scripting and it has so many features thats used to automate our boring tasks as well as other amazing cool features.

One of the good thing about automation is that you can use several keywords known by the bash shell i.e *for, while, until* and so on.

Bash gives you so much freedom and adventure to explore whatsoever that you want to do inside your bash terminal ranging from creating 100s of new files, directories or even mass delete (BE CAREFUL ON THAT!! WITH GREAT POWER COMES GREAT RESPONSIBITY "Uncle Ben")

## Loops and conditions
In bash, loops are accessed using the keywords `for`, `while` and `do`. These keywords are used for doing repetitive tasks without boring yourself on and on again.

> syntax:
for i in [COMMAND]
do
    COMMAND
done

while((condition))
do
    COMMAND
done

until(( false condition == True condition))
do
    COMMAND
done

case EXPRESSION in
  Pattern_Case_1)
   STATEMENTS
   ;;
 Pattern_Case_1)
   STATEMENTS
   ;;
 Pattern_Case_N)
   STATEMENTS
   ;;
 *)
   STATEMENTS
   ;;
esac

As for conditions, `if` and `else` are the keywords using for checking if a certain command is either *True or False* 