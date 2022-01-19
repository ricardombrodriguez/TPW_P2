import { Groups } from "./groups";

export interface Users{
    id : number;
    username:string;
    first_name: string;
    last_name:string;
    group:Groups;
}