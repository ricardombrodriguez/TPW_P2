import { Publication_Status } from "./publication_status";
import { Publication_Topics } from "./publication_topics";
import { Users } from "./users";

export interface Publication{
    id : number;
    title: string;
    content:string;
    author:Users;
    created_on:string;
    status:Publication_Status;
    topic:Publication_Topics;
}