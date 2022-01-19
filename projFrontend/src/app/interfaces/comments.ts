import { Publication } from "./publication";
import { Users } from "./users";

export interface Comments{
    id:number;
    comment:string;
    author:Users;
    publication:Publication;
}