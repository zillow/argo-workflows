function baseUrl(): string {
    const base = document.querySelector('base');
    return base ? base.getAttribute('href') || '/' : '/';
}

// joinBasePath joins the <base href> value with a UI/API path while collapsing
// any duplicate slashes at the join point. This protects callers that pass
// paths with or without a leading slash from producing URLs like
// "/argo-ui//archived-workflows/..." when BASE_HREF is "/argo-ui/".
function joinBasePath(base: string, path: string): string {
    const normalizedBase = (base || '/').replace(/\/+$/, '');
    const normalizedPath = (path || '').replace(/^\/+/, '');
    return normalizedPath ? `${normalizedBase}/${normalizedPath}` : `${normalizedBase}/`;
}

export function uiUrl(uiPath: string): string {
    return joinBasePath(baseUrl(), uiPath);
}

export function uiUrlWithParams(uiPath: string, params: string[]): string {
    const url = joinBasePath(baseUrl(), uiPath);
    return params && params.length > 0 ? `${url}?${params.join('&')}` : url;
}

export function apiUrl(apiPath: string): string {
    return joinBasePath(baseUrl(), apiPath);
}

export function absoluteUrl(path: string): string {
    const base = document.baseURI.endsWith('/') ? document.baseURI : document.baseURI + '/';
    return `${base}${path}`;
}
