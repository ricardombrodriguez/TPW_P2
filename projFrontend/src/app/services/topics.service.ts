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

  createTopic(form: FormGroup) {

    console.log("creating topic")



    
    let params = new HttpParams();
    params = params.append('description', form.value.description);
    return this.http.post(this.baseUrl + 'pubtopicscreate', {}, { params });
  }

}
