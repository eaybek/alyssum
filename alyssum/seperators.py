from termcolor import colored


class Title(object):
    """
    this class contains a helper function which you can configure every single instance differently
    """

    def __init__(self, label='', length=80, color='blue', design_char='#'):
        self.configure(label, length, color, design_char)

    def configure(self, label=None, length=None, color=None, design_char=None):
        if length is not None:
            if length < 0 or length > 80:
                raise Exception("Length must greater than 0 and smaller than 80")
            self.length = length
        if label is not None:
            if len(label) > self.length-2:
                raise Exception("label can not be greater than (length - 2) ")
            self.label = label
        if color is not None:
            if color not in ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
                raise Exception("color can be 'grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan' or 'white'")
            self.color = color
        if design_char is not None:
            if len(design_char) != 1:
                raise Exception("Design char length must be 1")
            self.design_char = design_char
        return self

    def write(self, label=None):
        """
        helper
        hashtag label function
        this function is print label in center of print(length*"#")
        label:  Message what you say
        length: Column number

        """
        if label is not None:
            self.configure(label=label)

        if self.length < 2:
            raise Exception("length must greater than 2")
        len_of_label = len(self.label)
        if len_of_label == 0:
            left_space = self.length/2
            rigth_space = self.length/2
        elif len_of_label < 0 or len_of_label > self.length - 2:
            raise Exception("Out of range")
        elif len_of_label % 2 == 0:
            left_space = (self.length - len_of_label) / 2
            if self.length % 2 == 0:
                rigth_space = left_space
            else:
                rigth_space = left_space+1
        elif len_of_label % 2 == 1:
            left_space = (self.length - len_of_label) / 2
            if self.length % 2 == 0:
                rigth_space = left_space+1
            else:
                rigth_space = left_space
        print(colored(self.length*self.design_char, self.color))
        print(colored(self.design_char, self.color), end='')
        print((int(left_space)-1)*" ", end='')
        print(colored(self.label.upper(), self.color), end='')
        print((int(rigth_space)-1)*" ", end='')
        print(colored(self.design_char, self.color))
        print(colored(self.length*self.design_char, self.color))
