#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <linux/in.h>
#include <linux/etherdevice.h>
#include <net/checksum.h>
#include <net/tcp.h>

#define FLAG "cratectf{FAKEFLAG}"

struct ip_ll {
    __be32 ip;    
    __be16 port;
    struct ip_ll * prev;
    struct ip_ll * next;
    __u8 won;
};

struct ip_ll * head;

noinline static struct ip_ll * ll_push(__be32 ip) {
    struct ip_ll * newi;
    struct ip_ll * ci = head;

    while(ci->next != NULL) ci = ci->next;

    ci->next = kmalloc(sizeof(struct ip_ll), GFP_ATOMIC);
    if (ci->next == NULL) return NULL;

    newi = ci->next;

    newi->next = NULL;
    newi->prev = ci;
    newi->ip = ip;
    newi->port = 0;
    newi->won = 0;

    return newi;
}

noinline static struct ip_ll * ll_find(__be32 ip) {
    struct ip_ll * ci = head;

    while(ci->next != NULL) {
        ci = ci->next;
        if (ip == ci->ip) return ci;
    }
    return NULL;
}

noinline static void ll_pop_element(__be32 ip) {
    struct ip_ll * prev, * next;
    struct ip_ll * di = ll_find(ip);

    if (di == NULL) return;

    prev = di->prev;
    next = di->next;

    prev->next = next;
    // only update next if not null 
    if(next) next->prev = prev;

    kfree(di);
}

noinline static void ll_destroy(void) {
    struct ip_ll * next;
    struct ip_ll * ci = head;

    while(ci != NULL) {
        next = ci->next;
        kfree(ci);
        ci = next;
    }
}

static unsigned int incoming_handler(void *priv, struct sk_buff *recv_skb, const struct nf_hook_state *state) {    
    struct ethhdr *recv_ethh;
    struct iphdr *recv_iph;
    struct tcphdr *recv_tcph; 
    uint8_t *recv_data;

    uint8_t password[8] = {0x7a, 0x3c, 0x2d, 0x6b, 0xdb, 0xf3, 0xf2, 0x99};
    if (!recv_skb)
        return NF_ACCEPT;

    recv_ethh = eth_hdr(recv_skb);
    recv_iph = ip_hdr(recv_skb);

    if (recv_iph->protocol == IPPROTO_TCP) {
        recv_tcph = tcp_hdr(recv_skb);
        recv_data = (unsigned char *)(recv_tcph + 1);

        if(memcmp(recv_data, password, 8) == 0) {
            struct ip_ll * ti = ll_find(recv_iph->saddr);
            if (ti == NULL) {
                ti = ll_push(recv_iph->saddr);
                if(ti == NULL) {
                    printk(KERN_INFO "Machine may be out of memory, contact administrators.");
                    return NF_ACCEPT;
                }
            }

            switch(ti->port) {
                case ntohs(0):
                    if (recv_tcph->dest == ntohs(1288)) {
                        ti->port = recv_tcph->dest;
                        return NF_DROP;
                    } else {
                        ll_pop_element(recv_iph->saddr);
                    };
                    
                    break;
                case ntohs(1288):
                    if (recv_tcph->dest == ntohs(5134)) {
                        ti->port = recv_tcph->dest;
                        return NF_DROP;
                    } else {
                        ll_pop_element(recv_iph->saddr);
                    };
                    
                    break;

                case ntohs(5134):
                    if (recv_tcph->dest == ntohs(36112)) {
                        ti->won = 1;
                        return NF_DROP;
                    } else {
                        ll_pop_element(recv_iph->saddr);
                    };
                    
                    break;

                default:
                    ll_pop_element(recv_iph->saddr);
                    break;
            }
            
        }
    }
    return NF_ACCEPT;
}

static unsigned int outgoing_handler(void *priv, struct sk_buff *recv_skb, const struct nf_hook_state *state) {
    struct ethhdr *recv_ethh;
    struct iphdr *recv_iph;
    struct tcphdr *recv_tcph; 
    uint8_t *recv_data;

    if (!recv_skb)
        return NF_ACCEPT;

    recv_ethh = eth_hdr(recv_skb);
    recv_iph = ip_hdr(recv_skb);
    int recv_iph_len = recv_iph->ihl * 4;

    if (recv_iph->protocol == IPPROTO_TCP) {
        recv_tcph = tcp_hdr(recv_skb);
        int recv_tcph_len = recv_tcph->doff * 4;

        int recv_data_len = ntohs(recv_iph->tot_len) - recv_iph_len - recv_tcph_len;

        if(recv_tcph->source == ntohs(50014) && recv_data_len > strlen(FLAG)) {
            struct ip_ll * ti = ll_find(recv_iph->daddr);

            if (ti == NULL ) return NF_ACCEPT;
            if (!ti->won) return NF_ACCEPT;

            if (skb_ensure_writable(recv_skb, recv_skb->len) != 0) return NF_ACCEPT; 
            if (skb_linearize(recv_skb) != 0) return NF_ACCEPT; 

            // grab new pointer after made writable
            
            recv_tcph = tcp_hdr(recv_skb);
            int recv_tcph_len = recv_tcph->doff * 4;

            recv_data = ((unsigned char *)recv_tcph) + recv_tcph_len;

            memcpy(recv_data, FLAG, strlen(FLAG));
            recv_tcph->check = 0;
            recv_tcph->check = tcp_v4_check(recv_skb->len - (recv_iph->ihl * 4),
                                       recv_iph->saddr,
                                       recv_iph->daddr,
                                       csum_partial(recv_tcph, recv_skb->len - (recv_iph->ihl * 4), 0));
            
            recv_iph->check = 0;
            recv_iph->check = ip_fast_csum((unsigned char *)recv_iph, recv_iph->ihl);

        }
    }
    return NF_ACCEPT;
}

static struct nf_hook_ops incoming_hook_ops = {
    .hook = incoming_handler,
    .pf = NFPROTO_IPV4,
    .hooknum = NF_INET_PRE_ROUTING,
    .priority = NF_IP_PRI_FIRST,
};

static struct nf_hook_ops outgoing_hook_ops = {
    .hook = outgoing_handler,
    .pf = NFPROTO_IPV4,
    .hooknum = NF_INET_POST_ROUTING,
    .priority = NF_IP_PRI_FIRST,
};

static int __init onload(void) {
    
    head = kmalloc(sizeof(struct ip_ll), GFP_ATOMIC);
    if (head == NULL) return -ENOMEM;

    memset((char *)head, 0, sizeof(struct ip_ll));

    nf_register_net_hook(&init_net, &incoming_hook_ops);
    nf_register_net_hook(&init_net, &outgoing_hook_ops);
    return 0;
}

static void __exit onunload(void) {

    ll_destroy();
    nf_unregister_net_hook(&init_net, &incoming_hook_ops);
    nf_unregister_net_hook(&init_net, &outgoing_hook_ops);
}

module_init(onload);
module_exit(onunload);

MODULE_LICENSE("Proprietary");
MODULE_AUTHOR("FOI");
MODULE_DESCRIPTION("");
