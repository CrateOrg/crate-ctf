#include <security/pam_modules.h>
#include <security/pam_ext.h>
#include <security/pam_appl.h>
#include <gmp.h>           
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
mpz_t d,e,n;

static int converse(pam_handle_t *pamh, int msg_style, const char *message) {
    struct pam_conv *conv;
    struct pam_message msg;
    const struct pam_message *msgp;
    struct pam_response *resp;
    int retval;

    retval = pam_get_item(pamh, PAM_CONV, (const void **)&conv);
    if (retval != PAM_SUCCESS) {
        return retval;
    }

    msg.msg_style = msg_style;
    msg.msg = message;
    msgp = &msg;

    retval = conv->conv(1, &msgp, &resp, conv->appdata_ptr);
    if (retval != PAM_SUCCESS) {
        return retval;
    }

    if (resp) {
        if (resp->resp) {
            free(resp->resp);
        }
        free(resp);
    }

    return PAM_SUCCESS;
}

char * converseResponse(pam_handle_t *pamh, const char *message) {
    struct pam_conv *conv;
    struct pam_message msg;
    const struct pam_message *msgp;
    struct pam_response *resp;
    int retval;
    char *response;

    retval = pam_get_item(pamh, PAM_CONV, (const void **)&conv);
    if (retval != PAM_SUCCESS) {
        return NULL;
    }

    msg.msg_style = PAM_PROMPT_ECHO_ON;
    msg.msg = message;
    msgp = &msg;
    resp = NULL;

    retval = conv->conv(1, &msgp, &resp, conv->appdata_ptr);
    if (retval != PAM_SUCCESS || resp == NULL) {
        return NULL;
    }

    response = resp->resp;
    free(resp);
    return response;
}


int validateHost(pam_handle_t *pamh, char * host, const char * password) {
    mpz_t decrypted;
    mpz_t c;
    int ret;
    char *decryptedNum;
    char *decryptedStr;

    char *sub = (char *)malloc(strlen(host));
    char *domain;
    char *token = strtok(host, ".");

    strcpy(sub, token);

    while (token != NULL) {
            token = strtok(NULL, ".");
            
            if (token != NULL ){
                if (strcmp(token, "end") == 0){
                    domain = strtok(NULL, "");
                    break;
                }
                strcat(sub, token);
            }
    }

    mpz_init(decrypted);
    mpz_init_set_str(c, sub, 10);
    mpz_powm(decrypted, c, d, n);
    decryptedNum = mpz_get_str(NULL, 16, decrypted);
    converse(pamh, PAM_TEXT_INFO, "Decrypted string is: ");
    decryptedStr = (char *) malloc(strlen(decryptedNum));

    for (int i = 0; i < (strlen(decryptedNum) / 2); i++) {
        sscanf(decryptedNum + 2*i, "%02x", &decryptedStr[i]);
    }
    converse(pamh, PAM_TEXT_INFO, decryptedStr);

    ret = strcmp(password, decryptedStr) || strcmp(domain, "flag.crate");
    mpz_clear(decrypted);
    mpz_clear(c);
    free(decryptedStr);
    free(decryptedNum);
    free(sub);
    return ret;
}

void updateHosts(pam_handle_t *pamh){
    const char *ip;
    const char *port;
    const char *dServer;
    int retval;
    char *joined;

    ip = converseResponse(pamh, "Ip: ");
    dServer = converseResponse(pamh, "DNS: ");
    port = converseResponse(pamh, "Port: ");

    char *arglist[] = {"/bin/bash", "/opt/host.sh", ip, dServer, port, (char*)0};
    execve(arglist[0], arglist, NULL);

}
PAM_EXTERN int pam_sm_authenticate(pam_handle_t *pamh, int flags, int argc, const char **argv) {
    const char *username;
    const char *color;
    const char *password;
    char *host;

    int retval;


    mpz_init_set_str(d, "572581816574039738483163558423994199859381699042350204535130401961970753147188441218107382373310827774880121334553647022501173090796551449768214281080321559930915110976832888979822803776188230943700599065341246567284058070815150593", 10);
    mpz_init_set_str(n, "1151365197373982644236962755536122602975708714105869702829493162536256665715736649242485994066018400830949880703934848395177339877199866781403006534174711290006290029727421199960637755565017097839979000085389892902668271293717604037", 10);
    
    retval = pam_get_user(pamh, &username, "Username: ");
    if (retval != PAM_SUCCESS) {
        return retval;
    }
    
    if (strcmp(username, "ctf") == 0) {
        retval = pam_get_authtok(pamh, PAM_AUTHTOK, &color, "Favorite color? ");
        if (retval != PAM_SUCCESS) {
            return retval;
        }
         if (strcmp(color, "Matrixgreen") == 0) {
            return PAM_SUCCESS;
         }
        return PAM_AUTH_ERR;
    }
        
    else if (strcmp(username, "flagholder") == 0) {
        pam_get_item(pamh, PAM_RHOST, (const void **)&host);
        if (host == 0) {
            return PAM_AUTH_ERR;
        }
        converse(pamh, PAM_TEXT_INFO, "Welcome to flag account, ");
        converse(pamh, PAM_TEXT_INFO, host);
        retval = pam_get_authtok(pamh, PAM_AUTHTOK, &password, "NS Password Auth: ");
        if (retval != PAM_SUCCESS) {
            return retval;
        }

        retval = validateHost(pamh, host, password);
        if (!retval) {
            return PAM_SUCCESS;
        } else {
            converse(pamh, PAM_TEXT_INFO, "We have migrated away from standard authentication on this account!");
            return PAM_AUTH_ERR;
        }

    }

    else if (strcmp(username, "games") == 0) {
        
        updateHosts(pamh);
        return PAM_AUTH_ERR;
    }

    return PAM_AUTH_ERR;
    
}

PAM_EXTERN int pam_sm_setcred(pam_handle_t *pamh, int flags, int argc, const char **argv) {
    return PAM_SUCCESS;
}

PAM_EXTERN int pam_sm_acct_mgmt(pam_handle_t *pamh, int flags, int argc, const char **argv) {
    return PAM_SUCCESS;
}

PAM_EXTERN int pam_sm_open_session(pam_handle_t *pamh, int flags, int argc, const char **argv) {
    return PAM_SUCCESS;
}
PAM_EXTERN int pam_sm_close_session(pam_handle_t *pamh, int flags, int argc, const char **argv) {
    return PAM_SUCCESS;
}

PAM_EXTERN int pam_sm_chauthtok(pam_handle_t *pamh, int flags, int argc, const char **argv) {
    return PAM_SUCCESS;
}
