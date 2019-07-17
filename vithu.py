static void splitString(string str) 
    { 
        StringBuilder alpha =  
                 new StringBuilder(); 
        StringBuilder num =  
                 new StringBuilder(); 
        StringBuilder special =  
                 new StringBuilder(); 
      
        for (int i = 0; i < str.Length; i++) 
        { 
            if (Char.IsDigit(str[i])) 
                num.Append(str[i]); 
            else if((str[i] >= 'A' &&  
                     str[i] <= 'Z') ||  
                     (str[i] >= 'a' &&  
                      str[i] <= 'z')) 
                alpha.Append(str[i]); 
            else
                special.Append(str[i]); 
        } 
      
        Console.WriteLine(alpha); 
        Console.WriteLine(num); 
        Console.WriteLine(special); 
    } 
   
    public static void Main() 
    { 
        string str = "geeks01$$for02geeks03!@!!"; 
        splitString(str); 
    } 
} 
