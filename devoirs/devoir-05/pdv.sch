<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2" xmlns:sqf="http://www.schematron-quickfix.com/validator/process">
    
    
    <sch:pattern>
        <sch:rule context="//ouverture">
            <sch:assert test="@debut and @fin">la balise ouverture a toujours un début</sch:assert>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern>
        <sch:rule context="//ville">
            <sch:report test="upper-case(text())">
                les noms des villes devraient être tous en majuscule pour la consistance    
            </sch:report>
        </sch:rule>
    </sch:pattern>
</sch:schema>