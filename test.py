import os
import sys
import importlib.util

def grade_files():
    current_script = os.path.basename(__file__)
    files = [f for f in os.listdir('.') if f.endswith('.py') and f != current_script]
    
    for filename in files:
        module_name = filename[:-3]
        spec = importlib.util.spec_from_file_location(module_name, filename)
        module = importlib.util.module_from_spec(spec)
        
        # redirect stdin to empty to prevent student input() from hanging
        sys.stdin = open(os.devnull, 'r')
        
        try:
            spec.loader.exec_module(module)
            # define test logic directly to avoid docstring complexities with dynamic imports
            john1 = """In the beginning was the Word, and the Word was with God, and the Word was God. 
He was in the beginning with God. All things were made through him, and without him was not any thing made that was made. 
In him was life, and the life was the light of men. 
The light shines in the darkness, and the darkness has not overcome it.

There was a man sent from God, whose name was John. 
He came as a witness, to bear witness about the light, that all might believe through him. 
He was not the light, but came to bear witness about the light.

The true light, which gives light to everyone, was coming into the world. 
He was in the world, and the world was made through him, yet the world did not know him. 
He came to his own, and his own people did not receive him. 
But to all who did receive him, who believed in his name, he gave the right to become children of God, who were born, not of blood nor of the will of the flesh nor of the will of man, but of God.

And the Word became flesh and dwelt among us, and we have seen his glory, glory as of the only Son from the Father, full of grace and truth."""
            
            results = [
                module.count_chars("Hello world") == 11,
                module.count_chars("") == 0,
                module.count_chars(john1) == 1103,
                module.count_words("Hello world") == 2,
                module.count_words("") == 0,
                module.count_sentences("Hello world. How are you? I am fine!") == 3,
                module.count_sentences(john1) == 13,
                module.count_paras("Para 1\n\nPara 2") == 2,
                module.count_paras(john1) == 4
            ]

            print(f"{sum(results)} of {len(results)} passed")

        except Exception as e:
            print(f"ERROR: {e}")
        
        print(f"Filename: {filename}")
        
        # restore stdin to wait for user input
        sys.stdin = sys.__stdin__
        input("Press enter to continue to the next test...")
        print("-" * 20)

if __name__ == "__main__":
    grade_files()
