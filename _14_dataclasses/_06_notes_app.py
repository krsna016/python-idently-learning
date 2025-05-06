import sys
from dataclasses import dataclass, field
from uuid import uuid4, UUID


@dataclass
class Note:
    id: UUID = field(init=False)
    title: str
    body: str

    def __post_init__(self) -> None:
        self.id = uuid4()


class NoteApp:
    def __init__(self, author: str, notes: list[Note] | None = None) -> None:
        self.author = author
        if notes is None:
            self._notes = []
        else:
            self._notes = notes
        self.display_instructions()

    @staticmethod
    def display_instructions() -> None:
        print("Welcome to the NoteApp!")
        print("Here are the available commands:")
        print("1. Add a new note")
        print("2. Edit the note")
        print("3. Delete a note by ID")
        print("4. Display all notes")
        print("5. Exit the application")

    def _add_note(self) -> None:
        title: str = input("Title : ")
        body: str = input("Body : ")
        note: Note = Note(title, body)
        self._notes.append(note)
        print("Note was added...")

    def _edit_note(self) -> None:
        print("Which note would you like to edit : ")
        self._show_notes()
        try:
            note_index: int = int(input('Index: ')) - 1
            current: Note = self._notes[note_index]
            new_title: str = input("New Title : ")
            new_body: str = input("New Body : ")
            current.title = new_title
            current.body = new_body
            print("Note Updated Successfully !!")
        except IndexError:
            print("Select Correct Note Index.")
            self._edit_note()
        except ValueError:
            print("Index cannot be Empty.")
            print("Aborting Operation...")

    def _delete_note(self) -> None:
        print("Which note would you like to delete : ")
        self._show_notes()
        try:
            note_index = int(input("Index : ")) - 1
            del self._notes[note_index]
            print("Note was deleted.")
        except IndexError:
            print("Select Correct Note Index.")
            self._delete_note()
        except ValueError:
            print("Index cannot be Empty.")
            print("Aborting Operation...")

    def _show_notes(self) -> None:
        if not self._notes:
            print("No Notes...")
            return
        for i, note in enumerate(self._notes, start=1):
            print(f'[{i}] {note.title}: {note.body}')

    def _exit_app(self) -> None:
        sys.exit()

    def _select_option(self, user_input: str) -> None:
        if user_input not in ['1', '2', '3', '4', '5']:
            print('Please pick a valid response...')
            return

        if user_input == '1':
            self._add_note()
        elif user_input == '2':
            self._edit_note()
        elif user_input == '3':
            self._delete_note()
        elif user_input == '4':
            self._show_notes()
        elif user_input == '5':
            self._exit_app()

    def run_app(self) -> None:
        while True:
            user_input: str = input("You : ")
            self._select_option(user_input)


def main() -> None:
    sample_notes = [
        Note(title="Grocery List", body="Buy milk, eggs, and bread."),
        Note(title="Meeting Notes", body="Discuss project timeline and deliverables."),
        Note(title="Workout Plan", body="Monday: Chest, Tuesday: Back, Wednesday: Legs."),
        Note(title="Book to Read", body="Start reading 'Atomic Habits' by James Clear."),
        Note(title="Birthday Reminder", body="John's birthday is on March 15th.")
    ]
    note_app: NoteApp = NoteApp("Anurag", sample_notes)
    note_app.run_app()


if __name__ == '__main__':
    main()
