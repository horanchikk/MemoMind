// @ts-ignore
import axios from "axios";


/**
 *
 * Provides working with MemoMind RestAPI
 */
export class MMAPI {
    private static readonly API_URL = "http://localhost:8000";
    private static readonly USER_URL = `${MMAPI.API_URL}/user`;
    private static readonly NOTE_URL = `${MMAPI.API_URL}/note`;
    private static readonly DESK_URL = `${MMAPI.API_URL}/desk`;

    private readonly access_token: string

    constructor(access_token: string) {
        this.access_token = access_token
    }

    private static async GET(url: string): Promise<MMError> {
        try {
            const response = await axios.get(url);
            return response.data.response;
        } catch (err) {
            return err.response.data;
        }
    }

    private static async POST(url: string, data: object = null): Promise<MMError> {
        try {
            const response = await axios.post(url, data);
            return response.data.response;
        } catch (err) {
            return err.response.data;
        }
    }

    private static async PATCH(url: string, data: object = null): Promise<MMError> {
        try {
            const response = await axios.patch(url, data);
            return response.data.response;
        } catch (err) {
            return err.response.data;
        }
    }

    private static async DELETE(url: string): Promise<MMError> {
        try {
            const response = await axios.delete(url);
            return response.data.response;
        } catch (err) {
            return err.response.data;
        }
    }

    /**
     * Registers user.
     *
     * E-mail should be unique.
     * Login should be unique.
     */
    public static async registerUser(
        login: string,
        password: string,
        firstName: string,
        lastName: string,
        email: string
    ): Promise<RegisterToken> {
        return await this.POST(`${this.USER_URL}/register`, {
            first_name: firstName,
            last_name: lastName,
            password: password,
            email: email,
            login: login,
        }) as RegisterToken;
    }

    /**
     * Logs in account via login and password
     */
    public static async logIn(login: string, password: string): Promise<UserToken> {
        return await this.POST(`${this.USER_URL}/login`, {
            login: login,
            password: password
        }) as UserToken;
    }

    /**
     * Gets user by ID
     */
    public static async getUserById(user_id: number): Promise<User> {
        return await this.GET(`${this.USER_URL}/id${user_id}`) as User;
    }

    /**
     * Changes user password
     */
    public async changePassword(old: string, newPass: string): Promise<UserToken> {
        return await MMAPI.PATCH(`${MMAPI.USER_URL}/edit?access_token=${this.access_token}`, {
            old_password: old,
            new_password: newPass
        }) as UserToken;
    }

    /**
     * Changes font in all notes and desks
     *
     * Returns "success".
     */
    public async changeFont(newFont: FontType): Promise<string | MMError> {
        return await MMAPI.PATCH(
            `${MMAPI.USER_URL}/font?font=${newFont}&access_token=${this.access_token}`
        );
    }

    /**
     * Changes compact view for all notes and desks
     *
     * Returns "success".
     */
    public async toggleCompact(value: boolean = true): Promise<string | MMError> {
        return await MMAPI.PATCH(
            `${MMAPI.USER_URL}/compact?access_token=${this.access_token}&value=${value}`
        );
    }

    /**
     * Changes small text for all notes and desks
     *
     * Returns "success".
     */
    public async toggleSmallText(value: boolean = true): Promise<string | MMError> {
        return await MMAPI.PATCH(
            `${MMAPI.USER_URL}/small_text?access_token=${this.access_token}&value=${value}`
        );
    }


    /**
     * Creates new note
     */
    public async createNote(title: string): Promise<CreatedNoteId> {
        return await MMAPI.POST(
            `${MMAPI.NOTE_URL}/?access_token=${this.access_token}`, {
                title: title
            }
        ) as CreatedNoteId;
    }

    /**
     * Returns note by ID
     */
    public async getNote(noteId: number): Promise<Note> {
        return await MMAPI.GET(`${MMAPI.NOTE_URL}/id${noteId}?access_token=${this.access_token}`) as Note;
    }

    /**
     * Edits note by ID
     *
     * Returns "success".
     */
    public async editNote(
        noteId: number,
        newTitle: string,
        data: string,
        cover: string = '',
        gradient: Array<string> = [ '#8A2387', '#E94057', '#F27121' ]
    ): Promise<string | MMError> {
        return await MMAPI.PATCH(
            `${MMAPI.NOTE_URL}/id${noteId}?access_token=${this.access_token}`, {
                title: newTitle,
                data: data,
                cover: cover,
                gradient: gradient
            }
        );
    }

    /**
     * Share note and makes it public.
     *
     * Returns "success".
     */
    public async shareNote(noteId: number, noteName: string): Promise<string | MMError> {
        return await MMAPI.PATCH(
            `${MMAPI.NOTE_URL}/share?access_token=${this.access_token}&note_name=${noteName}&note_id=${noteId}`
        );
    }

    /**
     * Unshares the note and makes it private.
     *
     * Returns "success".
     */
    public async unshareNote(noteId: number): Promise<string | MMError> {
        return await MMAPI.PATCH(
            `${MMAPI.NOTE_URL}/unshare?access_token=${this.access_token}&note_id=${noteId}`
        );
    }

    /**
     * Adds/removes note in favorite
     *
     * Returns true when added to favorite and false otherwise.
     */
    public async toggleFavorite(noteId: number): Promise<boolean | MMError> {
        return await MMAPI.PATCH(
            `${MMAPI.NOTE_URL}/favorite?access_token=${this.access_token}&note_id=${noteId}`
        );
    }

    /**
     * Moves note in trash or delete it forever
     *
     * Returns "success".
     */
    public async deleteNote(noteId: number): Promise<string | MMError> {
        return await MMAPI.DELETE(
            `${MMAPI.NOTE_URL}/id${noteId}?access_token=${this.access_token}`
        );
    }

    /**
     * Restores note from trash if available.
     *
     * Returns "success".
     */
    public async restoreNote(noteId: number): Promise<string | MMError> {
        return await MMAPI.PATCH(
            `${MMAPI.NOTE_URL}/restore${noteId}?access_token=${this.access_token}`
        );
    }

    /**
     * Returns public note
     */
    public static async getPublicNote(noteName: string): Promise<Note> {
        return await MMAPI.GET(
            `${MMAPI.NOTE_URL}/${noteName}`
        ) as Note;
    }

    /**
     * Creates a new desk
     */
    public async createDesk(title: string): Promise<CreatedDeskId> {
        return await MMAPI.POST(
            `${MMAPI.DESK_URL}/?access_token=${this.access_token}`, {
                title: title
            }
        ) as CreatedDeskId;
    }

    /**
     * Returns desk by ID
     */
    public async getDesk(deskId: number): Promise<Desk> {
        return await MMAPI.GET(
            `${MMAPI.DESK_URL}/id${deskId}?access_token=${this.access_token}`
        ) as Desk;
    }

    /**
     * Adds a new label into desk
     */
    public async addLabel(deskId: number, title: string, color: string): Promise<CreatedLabelIndex> {
        return await MMAPI.POST(
            `${MMAPI.DESK_URL}/label?access_token=${this.access_token}`, {
                did: deskId,
                title: title,
                color: color
            }
        ) as CreatedLabelIndex;
    }

    /**
     * Adds a new column into desk
     */
    public async addColumn(deskId: number, title: string): Promise<CreatedColumnIndex> {
        return await MMAPI.POST(
            `${MMAPI.DESK_URL}/column?access_token=${this.access_token}`, {
                did: deskId,
                title: title
            }
        ) as CreatedColumnIndex;
    }

    /**
     * Adds a new column into desk
     */
    public async addColumnCard(
        deskId: number,
        columnIndex: number,
        title: string,
        description: string = '',
        labels: Array<number> = [],
        properties: Array<object> = []
    ): Promise<CreatedColumnCardIndex> {
        return await MMAPI.POST(
            `${MMAPI.DESK_URL}/column-card?access_token=${this.access_token}`, {
                did: deskId,
                cid: columnIndex,
                title: title,
                description: description,
                labels: labels,
                properties: properties
            }
        ) as CreatedColumnCardIndex;
    }

    /**
     * Returns label by label index
     */
    public async getLabelByIndex(deskId: number, labelIndex: number): Promise<DeskCardLabel> {
        return await MMAPI.GET(
            `${MMAPI.DESK_URL}/id${deskId}/label${labelIndex}?access_token=${this.access_token}`
        ) as DeskCardLabel;
    }

    /**
     * Returns column by column index
     */
    public async getColumnByIndex(deskId: number, columnIndex: number): Promise<DeskColumn> {
        return await MMAPI.GET(
            `${MMAPI.DESK_URL}/id${deskId}/column${columnIndex}?access_token=${this.access_token}`
        ) as DeskColumn;
    }
}


export interface MMError {
    message: string
    code: number
}
export interface UserToken extends MMError{
    access_token: string
}
export interface RegisterToken extends UserToken {
    id: number
}
export interface CreatedNoteId extends MMError {
    id: number
}
export interface CreatedDeskId extends MMError {
    did: number
}
export interface CreatedLabelIndex extends MMError {
    label_index: number
}
export interface CreatedColumnIndex extends MMError {
    column_index: number
}
export interface CreatedColumnCardIndex extends MMError {
    card_index: number
}
export interface Note extends MMError {
    nid: number
    author: number
    title: string
    data: string
    cover: string
    gradient: Array<string>
    created_at: number
    edited_at: number
}
export interface User extends MMError {
    first_name: string
    last_name: string
    login: string
    email: string
    font: string
    compact: boolean
    small_text: boolean
    notes: Array<number>
    desks: Array<number>
    notes_favorite: Array<number>
    desks_favorite: Array<number>
    notes_trash: Array<number>
    desks_trash: Array<number>
}

export interface DeskCardLabel extends MMError {
    title: string
    color: string
}
export interface DeskCard extends MMError {
    title: string
    description: string
    labels: Array<number>
    properties: Array<object>
}
export interface DeskColumn extends MMError {
    cid: number
    title: string
    cards: Array<DeskCard>
}
export interface Desk extends MMError{
    did: number
    author: number
    title: string
    public: string
    created_at: string
    edited_at: string
    labels: Array<DeskCardLabel>
    columns: Array<DeskColumn>
}


export enum FontType {
    Default = "default",
    SansSerif = "serif",
    Mono = "mono"
}

// async function main() {
//     const token = (await MMAPI.logIn("someone1", "qwerty")).access_token;
//     const api = new MMAPI(token);
//
//     await api.changeFont(FontType.SansSerif);
//     let noteId = (await api.createNote('My new note'))['id'];
//     let note = (await api.getNote(noteId));
//     console.log(note);
//
//     console.log(await api.editNote(noteId, 'Fuck ..', ''));
//
//     await api.shareNote(noteId, 'fuck');
// }
//
// main().then(r => {});
