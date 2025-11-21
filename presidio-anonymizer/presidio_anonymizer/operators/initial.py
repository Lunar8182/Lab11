from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Redact the string - empty value."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return text with not white space and no trailing letters."""
        words = text.strip().split()
        newWord = []

        for w in words:
            prefix = ""
            initial_char = None

            for ch in w:
                if ch.isalnum():
                    initial_char = ch.upper()
                    break
                else:
                    prefix += ch

            if initial_char:
                if prefix:  
                    newWord.append(f"{prefix}{initial_char}")
                else:       
                    newWord.append(f"{initial_char}.")
            else:
                newWord.append(w)

        return " ".join(newWord)



    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
