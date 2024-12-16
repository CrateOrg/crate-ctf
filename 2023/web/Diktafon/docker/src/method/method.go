package method

import "net/http"

type Handler struct {
	Get     http.Handler
	Head    http.Handler
	Post    http.Handler
	Put     http.Handler
	Patch   http.Handler
	Delete  http.Handler
	Connect http.Handler
	Options http.Handler
	Trace   http.Handler
}

func (h Handler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		if h.Get != nil {
			h.Get.ServeHTTP(w, r)
			return
		}
	case http.MethodHead:
		if h.Head != nil {
			h.Head.ServeHTTP(w, r)
			return
		}
	case http.MethodPost:
		if h.Post != nil {
			h.Post.ServeHTTP(w, r)
			return
		}
	case http.MethodPut:
		if h.Put != nil {
			h.Put.ServeHTTP(w, r)
			return
		}
	case http.MethodPatch:
		if h.Patch != nil {
			h.Patch.ServeHTTP(w, r)
			return
		}
	case http.MethodDelete:
		if h.Delete != nil {
			h.Delete.ServeHTTP(w, r)
			return
		}
	case http.MethodConnect:
		if h.Connect != nil {
			h.Connect.ServeHTTP(w, r)
			return
		}
	case http.MethodOptions:
		if h.Options != nil {
			h.Options.ServeHTTP(w, r)
			return
		}
	case http.MethodTrace:
		if h.Trace != nil {
			h.Trace.ServeHTTP(w, r)
			return
		}
	}
	http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
}
