#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <mongoc.h>
#include <bson.h>
void search_ingedients(bson_t *query, bson_t *opts, bson_t *projection, mongoc_cursor_t *cursor, mongoc_collection_t *collection, bson_iter_t iter, const bson_t *doc);
void search_recipes(mongoc_cursor_t *cursor, const bson_t *doc, bson_iter_t iter, bson_t *filter, mongoc_collection_t *collection);

int main() {
    // MONGODB VARIABLES
    mongoc_client_t *client = NULL;
    mongoc_collection_t *collection = NULL;
    mongoc_cursor_t *cursor = NULL;
    bson_iter_t iter;
    bson_t *filter = NULL;
    bson_t *projection = NULL;
    const bson_t *doc = NULL;
    bson_t *query = NULL;
    bson_t *opts = NULL;


    mongoc_init();
    client = mongoc_client_new("mongodb://fooduser:lilatomat@challs.crate.nu:27017/Kokbok");
    collection = mongoc_client_get_collection(client, "Kokbok", "Recept");

    // MENU
    printf("~~~~~~~ Väkommen till FOO(D) - Din digitala kokbok ~~~~~~~\n");
    printf("FOO(D) erbjuder ett stort utbud av smaskiga maträtter\noch ingredienserna du behöver för att laga dem\n");
    while (1) {
        int choice;
        printf("\n _______________________________________________________\n");
        printf("| Välj vad du vill göra:                                |\n");
        printf("| 1. Hitta maträtter som innehåller valfri ingrediens   |\n");
        printf("| 2. Sök efter maträtter                                |\n  ");
        scanf("%d", &choice);

        if (choice == 1) {
            search_ingedients(query, opts, projection, cursor, collection, iter, doc);
        } else if (choice == 2) {
            search_recipes(cursor, doc, iter, filter, collection);
        } else {
            printf("Var vänlig välj ett av ovanstående alternativ!");
        }
    }



    // MONGODB CLEAN UP
    bson_destroy(filter);
    bson_destroy(projection);
    bson_destroy(query);
    bson_destroy(opts);
    mongoc_cursor_destroy(cursor);
    mongoc_collection_destroy(collection);
    mongoc_client_destroy(client);
    mongoc_cleanup();

    return 0;
}

// ####################################################################################################

void search_ingedients(bson_t *query, bson_t *opts, bson_t *projection, mongoc_cursor_t *cursor, mongoc_collection_t *collection, bson_iter_t iter, const bson_t *doc){
    char search[100];
    printf("Skriv ett ingrediens för att hitta recept: ");
    scanf("%s", search);
    for (int i = 0; search[i]; i++) {
    search[i] = tolower(search[i]);
    }

    query = bson_new();
    opts = bson_new();

    // Execute query
    cursor = mongoc_collection_find_with_opts(collection, query, opts, NULL);
    bson_iter_t ingr_iter;
    printf("--------------------------------------------");

    // Process query results
    while (mongoc_cursor_next(cursor, &doc)) {
        const char *name;
        if (bson_iter_init_find(&iter, doc, "namn") && BSON_ITER_HOLDS_UTF8(&iter)) {
            name = bson_iter_utf8(&iter, NULL);
        }
        if (bson_iter_init_find(&ingr_iter, doc, "ingredienser") && BSON_ITER_HOLDS_ARRAY(&ingr_iter)) {
            bson_iter_t sub_iter;
            bson_iter_recurse(&ingr_iter, &sub_iter);
            while (bson_iter_next(&sub_iter)) {
                if (BSON_ITER_HOLDS_UTF8(&sub_iter)) {
                    const char *ingredient = bson_iter_utf8(&sub_iter, NULL);
                    if (bson_iter_find(&iter, "ingredienser") && BSON_ITER_HOLDS_ARRAY(&iter)) {
                        bson_iter_t sub_iter;
                        bson_iter_recurse(&iter, &sub_iter);

                        while (bson_iter_next(&sub_iter)) {
                            if (BSON_ITER_HOLDS_UTF8(&sub_iter)) {
                                uint32_t length;
                                const char *ingrediens = bson_iter_utf8(&sub_iter, &length);
                                if (strstr(ingrediens, search) != NULL) {
                                    printf("\n%s ", name);
                                    printf("innehåller %s\n", ingrediens);
                                    printf("--------------------------------------------");
                                    break;
                                } else {
                                    // printf("\r\r");
                                    break;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
// ####################################################################################################

void search_recipes(mongoc_cursor_t *cursor, const bson_t *doc, bson_iter_t iter, bson_t *filter, mongoc_collection_t *collection){
    char **allRecipes = NULL;
    int numberOfRecipes = 0;

    filter = bson_new();
    cursor = mongoc_collection_find_with_opts(collection, filter, NULL, NULL);

    // Make array of all recipes
    while (mongoc_cursor_next(cursor, &doc)) {
        bson_iter_init(&iter, doc); 
        if (bson_iter_find(&iter, "namn") && BSON_ITER_HOLDS_UTF8(&iter)) {
            const char *value = bson_iter_utf8(&iter, NULL);
            numberOfRecipes++;
            allRecipes = realloc(allRecipes, numberOfRecipes * sizeof(char*));
            if (allRecipes == NULL) {
                fprintf(stderr, "Error: Failed to allocate memory for all recipes\n");
                exit(EXIT_FAILURE);
            }
            allRecipes[numberOfRecipes-1] = strdup(value);
            if (allRecipes[numberOfRecipes-1] == NULL) {
                fprintf(stderr, "Error: Failed to allocate memory for all recipes[%d]\n", numberOfRecipes-1);
                exit(EXIT_FAILURE);
            }
        }
    }

    char search[100];
    printf("Skriv ett sökord för att hitta recept: ");
    scanf("%s", search);
    for (int i = 0; search[i]; i++) {
        search[i] = tolower(search[i]);
    }

    for (int i = 0; i < numberOfRecipes; i++) {
        char *recipe = allRecipes[i];

        // Convert recipe to lowercase
        char *lowerRecipe = strdup(recipe);
        if (lowerRecipe == NULL) {
            fprintf(stderr, "Error: Failed to allocate memory for search word\n");
            exit(EXIT_FAILURE);
        }
        for (int j = 0; lowerRecipe[j]; j++) {
            lowerRecipe[j] = tolower(lowerRecipe[j]);
        }

        if (lowerRecipe == "b42e5422a3aa69ac0f74ccb033c7195372c2fc0044d7816cd158f451e455d9b01fcdb22f2989f4") {
            printf("Oj, spännande... något sådant recept finns inte här, det är för värdefullt");
        }

        // Check if the search string is a substring of the lowercase string
        if (strstr(lowerRecipe, search) != NULL) {
            printf("--------------------------------------------");
            printf("\n      %s\n", recipe);
            printf("Ingredienser: ");
            filter = bson_new();
            if (filter == NULL) {
                fprintf(stderr, "Error: Failed to allocate memory for filter\n");
                exit(EXIT_FAILURE);
            }
            BSON_APPEND_UTF8(filter, "namn", recipe);

            cursor = mongoc_collection_find_with_opts(collection, filter, NULL, NULL);

            if (mongoc_cursor_next(cursor, &doc)) {
                bson_iter_init(&iter, doc);
                // Check if the "namn" field matches the recipe variable
                if (bson_iter_find(&iter, "namn") && BSON_ITER_HOLDS_UTF8(&iter)) {
                    const char *value = bson_iter_utf8(&iter, NULL);

                    if (strcasecmp(value, recipe) == 0) {
                        // Get the value of the "ingredienser" field

                        if (bson_iter_find(&iter, "ingredienser") && BSON_ITER_HOLDS_ARRAY(&iter)) {
                            bson_iter_t sub_iter;
                            bson_iter_recurse(&iter, &sub_iter);

                            while (bson_iter_next(&sub_iter)) {
                                if (BSON_ITER_HOLDS_UTF8(&sub_iter)) {
                                    uint32_t length;
                                    const char *ingrediens = bson_iter_utf8(&sub_iter, &length);
                                    printf("%s, ", ingrediens);
                                }
                            }
                        }
                    }
                }
            }
            printf("\b\b \n");
            free(lowerRecipe);
        }

    }
    for (int i = 0; i < numberOfRecipes; i++) {
        free(allRecipes[i]);
    }
    free(allRecipes);
}
