# -*- encoding: utf-8 -*-
# stub: sinatra-activerecord 2.0.2 ruby lib

Gem::Specification.new do |s|
  s.name = "sinatra-activerecord"
  s.version = "2.0.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib"]
  s.authors = ["Blake Mizerany", "Janko Marohni\xC4\x87"]
  s.date = "2014-05-21"
  s.description = "Extends Sinatra with ActiveRecord helpers."
  s.email = "janko.marohnic@gmail.com"
  s.homepage = "http://github.com/janko-m/sinatra-activerecord"
  s.licenses = ["MIT"]
  s.required_ruby_version = Gem::Requirement.new(">= 1.9.2")
  s.rubygems_version = "2.2.2"
  s.summary = "Extends Sinatra with ActiveRecord helpers."

  s.installed_by_version = "2.2.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<sinatra>, ["~> 1.0"])
      s.add_runtime_dependency(%q<activerecord>, [">= 3.2"])
      s.add_development_dependency(%q<rake>, [">= 0"])
      s.add_development_dependency(%q<rspec>, [">= 2.10"])
      s.add_development_dependency(%q<sqlite3>, [">= 0"])
      s.add_development_dependency(%q<appraisal>, [">= 0"])
    else
      s.add_dependency(%q<sinatra>, ["~> 1.0"])
      s.add_dependency(%q<activerecord>, [">= 3.2"])
      s.add_dependency(%q<rake>, [">= 0"])
      s.add_dependency(%q<rspec>, [">= 2.10"])
      s.add_dependency(%q<sqlite3>, [">= 0"])
      s.add_dependency(%q<appraisal>, [">= 0"])
    end
  else
    s.add_dependency(%q<sinatra>, ["~> 1.0"])
    s.add_dependency(%q<activerecord>, [">= 3.2"])
    s.add_dependency(%q<rake>, [">= 0"])
    s.add_dependency(%q<rspec>, [">= 2.10"])
    s.add_dependency(%q<sqlite3>, [">= 0"])
    s.add_dependency(%q<appraisal>, [">= 0"])
  end
end
