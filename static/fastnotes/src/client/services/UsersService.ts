/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Body_signin } from '../models/Body_signin';
import type { UserCreate } from '../models/UserCreate';
import type { UserRead } from '../models/UserRead';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class UsersService {

    /**
     * Signup
     * @param requestBody
     * @returns UserRead Successful Response
     * @throws ApiError
     */
    public static signup(
        requestBody: UserCreate,
    ): CancelablePromise<UserRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/users/signup',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Signin
     * @param formData
     * @returns any Successful Response
     * @throws ApiError
     */
    public static signin(
        formData: Body_signin,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/users/signin',
            formData: formData,
            mediaType: 'application/x-www-form-urlencoded',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Current User
     * @returns UserRead Successful Response
     * @throws ApiError
     */
    public static getCurrentUser(): CancelablePromise<UserRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/users/me',
        });
    }

}
