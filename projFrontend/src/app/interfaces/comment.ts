import { Publication } from "./publication";
import { User } from "./user";

export interface Comment {
    id: number;
    comment: string;
    author: User;
    publication: Publication;
}