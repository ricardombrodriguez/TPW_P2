import { Publication } from "./publication";
import { User } from "./user";

export interface Favorite {
    id: number;
    author: User;
    publication: Publication;
}