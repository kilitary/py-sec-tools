rule _WinKript_v1_0__Mr_Crimson_esbyzz
{
	meta:
		description = "WinKript v1_0 __ Mr_ Crimson"
	strings:
		$a = {33C08BB800??????8B9004??????85FF741B33C950EB0C8A0439C0C804341B880439413BCA72F05883C008EBD561E9????????00000000000000000000000000000000000000000000000000000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
