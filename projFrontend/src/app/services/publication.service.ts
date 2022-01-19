import { Injectable } from '@angular/core';
import { Observable} from "rxjs/internal/Observable";
import {HttpClient, HttpHeaders} from "@angular/common/http";

const httpOptions = {
  headers : new HttpHeaders(  { 'Content-Type': 'application/json'})
};

@Injectable({
  providedIn: 'root'
})
export class PublicationService {

  private baseUrl='http://127.0.0.1:7007/ws/';
  constructor( private http: HttpClient) { }
}



/*
export class AuthorService {
  private baseUrl='http://127.0.0.1:7007/ws/';
  constructor( private http: HttpClient) { }

  getAuthor( id : number): Observable<AUTHOR> {
    const url= this.baseUrl+'author?id='+id;
    return this.http.get<AUTHOR>(url);
  }

  getAuthors( ): Observable<AUTHOR[]> {
    const url= this.baseUrl+'authors';
    return this.http.get<AUTHOR[]>(url);
  }

  getAuthorsN( num:number): Observable<AUTHOR[]> {
    const url= this.baseUrl+'authors?num='+num;
    return this.http.get<AUTHOR[]>(url);
  }

  createAuthor(au:AUTHOR) : Observable<any>{
    const url = this.baseUrl+'authorcre';
    return this.http.post(url, au, httpOptions);
  }

  updateAuthor(au:AUTHOR) : Observable<any>{
    const url = this.baseUrl+'authorupd';
    return this.http.put(url, au, httpOptions);
  }

  deleteAuthor(au:AUTHOR) : Observable<any>{
    const url = this.baseUrl+'authordel/'+ au.id;
    return this.http.delete<AUTHOR>(url,  httpOptions);
  }


}*/