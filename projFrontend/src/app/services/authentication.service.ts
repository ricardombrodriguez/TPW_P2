import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subject } from 'rxjs';
import { Authentication } from '../interfaces/authentication';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  userId = new Subject<string | null>()
  private baseUrl='http://127.0.0.1:7007/ws/';
  curentUserId = localStorage.getItem('user_id')

  constructor(private http: HttpClient) { 
    this.userId.next(localStorage.getItem('user_id'))
  }
  /*
  logIn = (email: string, password: string) =>
    this.http.get<AuthResponse>(environment.API_URL + '/login', {params: { email, password }}).subscribe(this.authResponseReaction)
  */
  }