rule _ASProtect_v____If_you_know_this_version_post_on_PEiD_board_h2__jbieyp
{
	meta:
		description = "ASProtect v___ __ If you know this version_ post on PEiD board _h2_"
	strings:
		$a = {33C0E9????FFFF??1C????40}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
