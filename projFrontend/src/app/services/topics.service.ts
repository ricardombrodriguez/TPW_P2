import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { Observable } from 'rxjs';
import { Publication_Topics } from '../interfaces/publication_topics';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class TopicsService {
  private baseUrl = 'http://127.0.0.1:7007/ws/';

  constructor(private http: HttpClient) { }

  getTopics(): Observable<Publication_Topics[]> {
    return this.http.get<Publication_Topics[]>(this.baseUrl + 'pubtopicsgetAll');
  }

  getEnabledTopics(): Observable<Publication_Topics[]> {
    return this.http.get<Publication_Topics[]>(this.baseUrl + 'pubtopicsenabledgetAll');
  }

  createTopic(form: FormGroup): Observable<any> {

    let topic: Publication_Topics = new Publication_Topics;
    topic.description = form.value.description;
    topic.enabled = form.value.enabled;
    return this.http.post(this.baseUrl + 'pubtopicscreate', topic, httpOptions);
  }

  updateTopic(topic: Publication_Topics, description: string): Observable<any> {

    topic.description = description;
    return this.http.put(this.baseUrl + 'pubtopicsupdate', topic, httpOptions);
  }

  disableTopic(topic: Publication_Topics): Observable<any> {

    return this.http.put(this.baseUrl + 'pubtopicsdisable', topic, httpOptions);
  }



}
