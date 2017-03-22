

class WPItemCreator:

    # %(project)s
    # %(slug)s
    #  d['url']
    # d['category']
    # d['address']
    # d['size']
    # d['cost']
    # d['description']
    # d['owner']
    # d['architect']
    # d['architectWebsite']
    def CreateItem(self, itemData):
        xmlItemTemplate = """<item>
	<title>%(project)s</title>
	<link>https://becaustin.wpengine.com/project/%(slug)s/</link>
	<pubDate>Wed, 08 Mar 2017 16:32:06 +0000</pubDate>
	<dc:creator><![CDATA[tmarc]]></dc:creator>
	<description></description>
	<content:encoded><![CDATA[Page Content (gallery will go here)]]></content:encoded>
	<excerpt:encoded><![CDATA[]]></excerpt:encoded>
	<wp:post_date><![CDATA[2017-03-08 10:32:06]]></wp:post_date>
	<wp:post_date_gmt><![CDATA[2017-03-08 16:32:06]]></wp:post_date_gmt>
	<wp:comment_status><![CDATA[closed]]></wp:comment_status>
	<wp:ping_status><![CDATA[closed]]></wp:ping_status>
	<wp:post_name><![CDATA[lower-case-title-value-goes-here]]></wp:post_name>
	<wp:status><![CDATA[publish]]></wp:status>
	<wp:post_parent>0</wp:post_parent>
	<wp:menu_order>0</wp:menu_order>
	<wp:post_type><![CDATA[project]]></wp:post_type>
	<wp:post_password><![CDATA[]]></wp:post_password>
	<wp:is_sticky>0</wp:is_sticky>
	<category domain="project_category" nicename="category-value-goes-here"><![CDATA[Category Value goes here]]></category>
	<wp:postmeta>
		<wp:meta_key><![CDATA[_prlipro-post-options]]></wp:meta_key>
		<wp:meta_value><![CDATA[a:3:{s:14:"requested_slug";s:0:"";s:19:"hide_social_buttons";b:0;s:20:"disable_replacements";b:0;}]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[_prlipro-post-options]]></wp:meta_key>
		<wp:meta_value><![CDATA[a:3:{s:14:"requested_slug";s:0:"";s:19:"hide_social_buttons";b:0;s:20:"disable_replacements";b:0;}]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[address]]></wp:meta_key>
		<wp:meta_value><![CDATA[Address Value Goes Here]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[_address]]></wp:meta_key>
		<wp:meta_value><![CDATA[field_58c02fec768dc]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[size]]></wp:meta_key>
		<wp:meta_value><![CDATA[Size Value Goes Here]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[_size]]></wp:meta_key>
		<wp:meta_value><![CDATA[field_58c0301d768dd]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[construction_cost]]></wp:meta_key>
		<wp:meta_value><![CDATA[Cost Value Goes Here]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[_construction_cost]]></wp:meta_key>
		<wp:meta_value><![CDATA[field_58c03039768de]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[description]]></wp:meta_key>
		<wp:meta_value><![CDATA[Description Value Goes Here]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[_description]]></wp:meta_key>
		<wp:meta_value><![CDATA[field_58c03047768df]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[owner]]></wp:meta_key>
		<wp:meta_value><![CDATA[Owner Value Goes Here]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[_owner]]></wp:meta_key>
		<wp:meta_value><![CDATA[field_58c03052768e0]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[architect]]></wp:meta_key>
		<wp:meta_value><![CDATA[Architect Value Goes Here]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[_architect]]></wp:meta_key>
		<wp:meta_value><![CDATA[field_58c03063768e1]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[architect_website]]></wp:meta_key>
		<wp:meta_value><![CDATA[Website Value Goes Here]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[_architect_website]]></wp:meta_key>
		<wp:meta_value><![CDATA[field_58c03071768e2]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[_edit_last]]></wp:meta_key>
		<wp:meta_value><![CDATA[5]]></wp:meta_value>
	</wp:postmeta>
	<wp:postmeta>
		<wp:meta_key><![CDATA[_wp_old_slug]]></wp:meta_key>
		<wp:meta_value><![CDATA[test-slug]]></wp:meta_value>
	</wp:postmeta>
</item>
"""
        #print( xmlItemTemplate%itemData )
        return xmlItemTemplate%itemData