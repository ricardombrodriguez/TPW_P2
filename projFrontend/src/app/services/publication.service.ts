import { Injectable } from '@angular/core';
import { Observable } from "rxjs/internal/Observable";
import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";
import { Publication } from '../interfaces/publication';
import { FormGroup } from '@angular/forms';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class PublicationService {

  private baseUrl = 'http://127.0.0.1:7007/ws/';

  constructor(private http: HttpClient) { }

  getPublication(id: number): Observable<Publication> {
    return this.http.get<Publication>(this.baseUrl + 'pub?id=' + id);
  }

  createPublication(form: FormGroup) {
    let params = new HttpParams();
    params = params.append('title', form.value.title);
    params = params.append('topic', form.value.topic);
    params = params.append('content', form.value.content);
    return this.http.post(this.baseUrl + 'pubcrate', {}, { params });
  }

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

  getSearchPublicationsApproved(author: string, date: string, topic: string, title: string): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getSearchPublicationsApproved?author=' + author + '&&date=' + date + '&&topic=' + topic + '&&title=' + title);
  }
  getSearchPublicationsFilled(author: string, date: string, topic: string, title: string): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getSearchPublicationsFilled?author=' + author + '&&date=' + date + '&&topic=' + topic + '&&title=' + title);
  }
  getSearchPublicationsPendent(author: string, date: string, topic: string, title: string): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getSearchPublicationsPendent?author=' + author + '&&date=' + date + '&&topic=' + topic + '&&title=' + title);
  }

  getSearchPublicationsApprovedByUser(id:number, date: string, topic: string, title: string): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getSearchPublicationsApprovedByUser?id='+id+ '&&date=' + date + '&&topic=' + topic + '&&title=' + title);
  }
  getSearchPublicationsFilledByUser(id:number, date: string, topic: string, title: string): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getSearchPublicationsFilledByUser?id='+id+ '&&date=' + date + '&&topic=' + topic + '&&title=' + title);
  }
  getSearchPublicationsPendentByUser(id:number, date: string, topic: string, title: string): Observable<Publication[]> {
    return this.http.get<Publication[]>(this.baseUrl + 'getSearchPublicationsPendentByUser?id='+id+ '&&date=' + date + '&&topic=' + topic + '&&title=' + title);
  }

}
