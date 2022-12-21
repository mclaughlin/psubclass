# psubclass

Simple script to output (in a pretty format) a class' subclasses.

```
Usage:
    python3 psubclass.py <class_name>

Example:
    python3 psubclass.py Exception

Example (from the REPL):
    >>> import psubclass
    >>> psubclass.main()
    Name of the class to find subclasses of: Exception

Example output:
    + ArgumentError
    + ArgumentTypeError
    + ArithmeticError
    |-- + FloatingPointError
    |-- + OverflowError
    |-- + ZeroDivisionError
    + AssertionError
    + AttributeError
    + BufferError
    + ClassFoundException
    + EOFError
    + EndOfBlock
    + Error
    + ImportError
    |-- + ModuleNotFoundError
    |-- + ZipImportError
    + LookupError
    |-- + CodecRegistryError
    |-- + IndexError
    |-- + KeyError
    + MemoryError
    + NameError
    |-- + UnboundLocalError
    + OSError
    |-- + BlockingIOError
    |-- + ChildProcessError
    |-- + ConnectionError
    |-- |-- + BrokenPipeError
    |-- |-- + ConnectionAbortedError
    |-- |-- + ConnectionRefusedError
    |-- |-- + ConnectionResetError
    |-- + FileExistsError
    |-- + FileNotFoundError
    |-- + InterruptedError
    |-- + IsADirectoryError
    |-- + NotADirectoryError
    |-- + PermissionError
    |-- + ProcessLookupError
    |-- + TimeoutError
    |-- + UnsupportedOperation
    |-- + itimer_error
    + ReferenceError
    + RuntimeError
    |-- + NotImplementedError
    |-- + RecursionError
    |-- + _DeadlockError
    + StopAsyncIteration
    + StopIteration
    + StopTokenizing
    + SyntaxError
    |-- + IndentationError
    |-- |-- + TabError
    + SystemError
    |-- + CodecRegistryError
    + TokenError
    + TypeError
    + ValueError
    |-- + UnicodeError
    |-- |-- + UnicodeDecodeError
    |-- |-- + UnicodeEncodeError
    |-- |-- + UnicodeTranslateError
    |-- + UnsupportedOperation
    + Verbose
    + Warning
    |-- + BytesWarning
    |-- + DeprecationWarning
    |-- + EncodingWarning
    |-- + FutureWarning
    |-- + ImportWarning
    |-- + PendingDeprecationWarning
    |-- + ResourceWarning
    |-- + RuntimeWarning
    |-- + SyntaxWarning
    |-- + UnicodeWarning
    |-- + UserWarning
    + _OptionError
    + error

```
