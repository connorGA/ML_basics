# BASIC CONCEPTS

    # variables in Python are symbolic names that reference or point to data stored in memory
    # variables are dynamically typed, meaning you dont need to declare their type before using them. The type is inferred from the assigned value

# Types of Variables

    # Numeric Types: Integers('int')
    #                floating-point numbers('float')
    #                complex numbers('complex')
    # Sequence Types: Lists('list')
    #                 tuples('tuple')
    #                 strings('str')
    # Mapping Type: Dictionary('dict') - Key value pairs are invaluable for mapping feature names to their values, storing model parameters or configuration settings             
    # Boolean Type:('bool') - Represents two values, True or False

# Variable Scope

    # Global Variables: Declared outside of a function and accessible anywhere in the script
    # Local Variables: Declared within a function and only accessible within that functions scope

# Mutable and Immutable Variables

    # Immutable Variables: Cannot be altered after creation. Examples include integers, floats, strings and tuples. Immutable variables ensure data integrity when constants or fixed parameters are required
    # Mutable Variables: Can be modified after creation. Lists, dictionaries, and instances of most custom classes.

# Use in Machine Learning

    # Data Representation: Variables store datasets, either in raw form or after preprocessing. They can represent features, labels, or entire dataframes(using libraries like pandas)
    # Model Parameters: Weights, biases, and hyperparameters are stored in variables. The flexibility of Python variables facilitates the dynamic adjustment and optimization of these parameters during training
    # Control Flow: Variables control the execution of training loops, conditional processing of data, and the application of algorithms based on model performance or validation outcomes
    # State Management: In more complex machine learning tasks, such as reinforcement learning or deep learning, variables manage the state of the model, learning rate schedules, or the internal state of recurrent neural networks