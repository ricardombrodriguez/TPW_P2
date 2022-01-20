import { Injectable } from '@angular/core';
import { Observable } from "rxjs/internal/Observable";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Publication } from '../interfaces/publication';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class PublicationService {

  private baseUrl = 'http://127.0.0.1:7007/ws/';

  constructor(private http: HttpClient) { }

  getActivePublications(): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getPublicationsApproved');
  }

  getPendentPublications(): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getPublicationsPendent');
  }

  getClosedPublications(): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getPublicationsFiled');
  }

  getActivePublicationsByUser(id: number): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getAuthorPublicationsApproved?id=' + id);
  }

  getPendentPublicationsByUser(id: number): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getAuthorPublicationsPendent?id=' + id);
  }

  getClosedPublicationsByUser(id: number): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getAuthorPublicationsFiled?id=' + id);
  }

  getFavouritePublicationsByUser(id: number): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getAuthorFavoritePublications?id=' + id);
  }

  getSearchPublications(author: string, date: string, topic: string, title: string): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getSearchPublications?author=' + author + '&&date=' + date + '&&topic=' + topic + '&&title=' + title);
  }
}
