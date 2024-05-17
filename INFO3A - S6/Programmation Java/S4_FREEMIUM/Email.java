import java.util.Objects;

class Email {
   String name;
   String domain;
   String domainName;

   Email(String name, String domain, String domainName){
      this.name = name;
      this.domain = domain;
      this.domainName = domainName;
   }

   @Override
   public int hashCode() {
     return this.toString().hashCode();
   }

   @Override
   public boolean equals(Object obj) {

      if (obj instanceof Email email) {
          return Objects.equals(email.name, this.name)
                 && Objects.equals(email.domain, this.domain)
                 && Objects.equals(email.domainName, this.domainName);
      }

      return false;
   }

   @Override
   public String toString() {
      return "%s@%s.%s".formatted(name, domain, domainName);
   }

}
