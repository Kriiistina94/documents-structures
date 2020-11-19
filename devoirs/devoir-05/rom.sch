<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2"
    xmlns:sqf="http://www.schematron-quickfix.com/validator/process">
    
        <sch:pattern abstract="true" id="structure-minimale">
            <sch:rule context="TEI">
                <sch:assert test="teiHeader and text">Le document contient une balise teiHeaer et une balise text</sch:assert>
            </sch:rule>
        </sch:pattern>
    
        <sch:pattern>
            <sch:rule context="sp">
                <sch:assert test="p">La balise sp doit contenir un paragraphe</sch:assert>
            </sch:rule>
        </sch:pattern>
    
        <sch:pattern>
            <sch:rule context="projectDesc">
                <sch:assert test="p">La projectDesc sp doit contenir un paragraphe</sch:assert>
            </sch:rule>
        </sch:pattern>
        
        <sch:pattern>
            <sch:rule context="div">
                <sch:let name="div" value="//div"/>
                <sch:assert test="$div/count(head) >= 1 ">La balise div doit contenir un élément head</sch:assert>
          </sch:rule>
        </sch:pattern>
    
</sch:schema>