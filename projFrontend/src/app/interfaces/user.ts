import { Group } from "./group";

export interface User {
    id: number;
    username: string;
    first_name: string;
    last_name: string;
    group: Group;
}