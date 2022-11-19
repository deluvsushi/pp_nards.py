import requests

class PPNards:
	def __init__(self) -> None:
		self.api = "https://game-api-v2.ppnards.com"
		self.headers = {
			"user-agent": "UnityPlayer/2021.3.0f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)",
			"x-unity-version": "2021.3.0f1"
		}
		self.user_id = None
		self.short_id = None
		self.access_token = None

	def get_version_info(self) -> dict:
		return requests.get(
			f"{self.api}/version",
			headers=self.headers).json()

	def sign_up(
			self,
			login: str, 
			password: str) -> dict:
		data = {
			"login": login,
			"password": password
		}
		return requests.post(
			f"{self.api}/signup",
			json=data,
			headers=self.headers).json()

	def login(
			self,
			login: str,
			password: str) -> dict:
		data = {
			"login": login,
			"password": password
		}
		response = requests.post(
			f"{self.api}/login",
			json=data,
			headers=self.headers).json()
		if "access_token" in response:
			self.access_token = response["access_token"]
			self.headers["authorization"] = f"Bearer {self.access_token}"
			account_info = self.get_account_info()
			self.user_id = account_info["id"]
			self.short_id = account_info["short_id"]
		return response

	def get_account_info(self) -> dict:
		return requests.get(
			f"{self.api}/api/account",
			headers=self.headers).json()

	def get_common_defaults(self) -> dict:
		return requests.get(
			f"{self.api}/api/common/defaults",
			headers=self.headers).json()

	def get_tournaments_list(
			self,
			filter: str = "all",
			status: str = "upcoming") -> dict:
		return requests.get(
			f"{self.api}/api/tournaments?tournaments_list_filter={filter}&status={status}",
			headers=self.headers).json()

	def get_shop_items(self) -> dict:
		return requests.get(
			f"{self.api}/api/shop/items",
			headers=self.headers).json()

	def update_profile(
			self,
			first_name: str = None,
			last_name: str = None,
			country: str = None,
			nickname: str = None,
			language: str = None,
			avatar: str = None,
			global_tournaments_available: bool = True) -> dict:
		data = {}
		if first_name:
			data["firstname"] = first_name
		if last_name:
			data["lastname"] = last_name
		if country:
			data["country"] = country
		if nickname:
			data["nickname"] = nickname
		if language:
			data["lang"] = language
		if avatar:
			data["avatar"] = avatar
		if global_tournaments_available:
			data["global_tournaments_available"] = global_tournaments_available
		return requests.post(
			f"{self.api}/api/account/update-profile",
			json=data,
			headers=self.headers).json()

	def get_bonus(self, bonus_type: str = "first_enter_bonus") -> dict:
		return requests.get(
			f"{self.api}/api/account/bonus/{bonus_type}",
			headers=self.headers).json()

	def get_account_clubs(self) -> dict:
		return requests.get(
			f"{self.api}/api/account/clubs",
			headers=self.headers).json()

	def get_sent_club_membership_requests(self) -> dict:
		return requests.get(
			f"{self.api}/api/account/club-membership-requests",
			headers=self.headers).json()

	def join_to_club(self, short_id: int) -> dict:
		return requests.get(
			f"{self.api}/club/by-short-id/{short_id}/info",
			headers=self.headers).json()

	def create_club(self) -> dict:
		return requests.post(
			f"{self.api}/api/club",
			headers=self.headers).json()

	def get_club_info(self, club_id: str) -> dict:
		return requests.get(
			f"{self.api}/api/club/{club_id}/info",
			headers=self.headers).json()

	def get_club_contacts(self, club_id: str) -> dict:
		return requests.get(
			f"{self.api}/api/club/{club_id}/get-contacts",
			headers=self.headers).json()

	def change_club_description(self, club_id: str, description: str) -> dict:
		return requests.post(
			f"{self.api}/api/club/{club_id}/change-description?club_id={club_id}&new_description={description}",
			headers=self.headers).json()

	def change_club_title(self, club_id: str, title: str) -> dict:
		return requests.post(
			f"{self.api}/api/club/{club_id}/change-title?club_id={club_id}&new_title={title}",
			headers=self.headers).json()

	def share_club_url(self, club_id: str, language: str = "ru") -> dict:
		return requests.get(
			f"{self.api}/api/club/{club_id}/share-url?club_id={club_id}&lang={language}",
			headers=self.headers).json()

	def get_club_membership_requests(self, club_id: str) -> dict:
		return requests.get(
			f"{self.api}/api/club/{club_id}/membership-requests",
			headers=self.headers).json()

	def get_club_members(
			self,
			club_id: str,
			order_by: str = "last_week_commission",
			ordering: str = "desc") -> dict:
		return requests.get(
			f"{self.api}/api/club/{club_id}/members?order_by={order_by}&ordering={ordering}",
			headers=self.headers).json()

	def delete_club(self, club_id: str) -> dict:
		return requests.get(
			f"{self.api}/api/club/{club_id}/terminate",
			headers=self.headers).json()

	def get_tournament_status(self, tournament_id: str) -> dict:
		return requests.get(
			f"{self.api}/api/tournaments/{tournament_id}/status",
			headers=self.headers).json()

	def get_tournament_info(self, tournament_id: str) -> dict:
		return requests.get(
			f"{self.api}/api/tournaments/{tournament_id}",
			headers=self.headers).json()

	def enroll_tournament(self, tournament_id: str) -> dict:
		return requests.post(
			f"{self.api}/api/tournaments/{tournament_id}/enroll",
			headers=self.headers).json()

	def get_tournament_prize_table(self, tournament_id: str) -> dict:
		return requests.get(
			f"{self.api}/api/tournaments/{tournament_id}/prize_table",
			headers=self.headers).json()

	def get_tournament_participants(self, tournament_id: str) -> dict:
		return requests.get(
			f"{self.api}/api/tournaments/{tournament_id}/participants",
			headers=self.headers).json()

	def get_tournament_layers(self, tournament_id: str) -> dict:
		return requests.get(
			f"{self.api}/api/tournaments/{tournament_id}/layers",
			headers=self.headers).json()

	def change_password(
			self,
			old_password: str,
			new_password: str) -> dict:
		data = {
			"old_password": old_password,
			"new_password": new_password
		}
		return requests.post(
			f"{self.api}/api/account/change-password",
			json=data,
			headers=self.headers).json()

	def delete_account(self) -> dict:
		return requests.delete(
			f"{self.api}/api/account",
			headers=self.headers).json()
