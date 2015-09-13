def playWithPlainExceptions():
    print("=== Plain Excetpions ===");
    d = {};
    try:
        print(d["test"]);
    except KeyError:
        print("Bad key");

    try:
        print(d["test"]);
    except KeyError as error:
        print(error);

    d["test"] = 0;

    try:
        print(1 / d["test"])
    except (NameError, ZeroDivisionError) as err: # catch all exceptions
        print(err)

    try:
        print(1 / d["test"])
    except: # catch all exceptions
        print("An error has occured")

def playWithExtrConstructs(a):
    print("=== Extra Exceptions ===");
    l = [1];
    try:
        print(l[0]);
    except:
        print("Index access error");
    else: # no excetion in try block
        print("Index access is ok");
    
    try:
        try:
            raise ValueError("Error"); # throw own exception
        except NameError:
            print("Unreachable");
        else:
            print("Unreachable");
        finally: # executes _always_ after try block
            print("Finally I'm here");
    except ValueError:
        pass;

    print("* Else vs Finally priority");
    try:
        l[0] += 13;
    # order matters: finally is the last; else _after_ except
    except:
        pass;
    else: # must be used after except and before finally
        print("Try is ok, l[0] is", l[0]);
    finally:
        print("Finally l[0] is", l[0]);

    print("* Exception rethrow");
    try:
        try:
            raise Error("Test");
        except:
            print("Inner try exception catched");
            raise;
    except:
        print("Outer try exception catched");

# custom error definition
class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg;
    def __str__(self):
        return self.msg;

def playWithCustomException():
    print("=== Custom exception ===");
    try:
        raise CustomException("I'm custom");
    except ValueError:
        print("Value Error");
    except CustomException as err:
        print(err);
    else:
        print("Unreachable");

if __name__ == "__main__":
    playWithPlainExceptions();
    playWithExtraConstructs();
    playWithCustomException();

