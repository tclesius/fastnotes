/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { NoteCreate } from '../models/NoteCreate';
import type { NoteRead } from '../models/NoteRead';
import type { NoteUpdate } from '../models/NoteUpdate';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class NotesService {

    /**
     * Get Notes
     * @param skip
     * @param limit
     * @returns NoteRead Successful Response
     * @throws ApiError
     */
    public static getNotes(
        skip: number,
        limit: number,
    ): CancelablePromise<Array<NoteRead>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/notes',
            query: {
                'skip': skip,
                'limit': limit,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Create Note
     * @param requestBody
     * @returns NoteRead Successful Response
     * @throws ApiError
     */
    public static createNote(
        requestBody: NoteCreate,
    ): CancelablePromise<NoteRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/notes',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Search Notes
     * @param query
     * @returns NoteRead Successful Response
     * @throws ApiError
     */
    public static searchNotes(
        query: string,
    ): CancelablePromise<Array<NoteRead>> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/notes/{query}',
            path: {
                'query': query,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Note
     * @param noteId
     * @returns NoteRead Successful Response
     * @throws ApiError
     */
    public static getNote(
        noteId: number,
    ): CancelablePromise<NoteRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/notes/{note_id}',
            path: {
                'note_id': noteId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Delete Note
     * @param noteId
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteNote(
        noteId: number,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/notes/{note_id}',
            path: {
                'note_id': noteId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Note
     * @param noteId
     * @param requestBody
     * @returns NoteRead Successful Response
     * @throws ApiError
     */
    public static updateNote(
        noteId: number,
        requestBody: NoteUpdate,
    ): CancelablePromise<NoteRead> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/notes/{note_id}',
            path: {
                'note_id': noteId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
