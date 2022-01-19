import { Publication } from "./publication";
import { Users } from "./users";

export interface Favorites{
    id : number;
    author:Users;
    publication:Publication;
}