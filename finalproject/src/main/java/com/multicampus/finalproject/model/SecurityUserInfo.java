 
package com.multicampus.finalproject.model;

import org.springframework.security.core.userdetails.User;

import lombok.Data;


// Spring security의 User객체를 상속받는 객체
// Spring security Context에 의해 로그인 세션이 유지된다.
@Data
public class SecurityUserInfo extends User{
    
    private static final long serialVersionUID = 1L;
    
    private String ip;
    
    public SecurityUserInfo(UserInfo userinfo) {
        super(userinfo.getUsername(), userinfo.getPassword(), userinfo.getAuthorities());
    }
    
    
}
    