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


/*

export class AuthenticationService {

  userId = new Subject<string | null>()
  userIdObs = this.userId.asObservable()

  curentUserId = localStorage.getItem('user_id')

  isLoggedIn = () => localStorage.getItem('user_id') !== null

  setUserId = (id: string | null = null) => {
    id === null? localStorage.removeItem('user_id') : localStorage.setItem('user_id', id)
    this.userId.next(id)
    this.curentUserId = id
  }

  signUp = (username: string, fullname: string, email: string, password: string) => 
    this.http.post<AuthResponse>(environment.API_URL + '/signup', { username, fullname, email, password }).subscribe(this.authResponseReaction)

  logIn = (email: string, password: string) =>
    this.http.get<AuthResponse>(environment.API_URL + '/login', {params: { email, password }}).subscribe(this.authResponseReaction)

  authResponseReaction = (response: AuthResponse) => this.setUserId(response.success ? response.id.toString() : null)

  logOut = () => this.setUserId()

  constructor(private http: HttpClient) { 
    this.userId.next(localStorage.getItem('user_id'))
  }
}*/