#!/usr/bin/env python3
"""Test script to verify the improved camel_to_snake function handles acronyms correctly."""

import pytest
import sys
import os

# Add the parent directory to the path to import generate modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils import camel_to_snake


class TestAcronymHandling:
    """Test cases for acronym handling improvement."""

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("OAuth2ClientInfo", "oauth2_client_info"),   # Hardcoded fix for OAuth2
            ("XMLHttpRequest", "xml_http_request"),       # Should be xml, not x_m_l
            ("APIKey", "api_key"),                        # Should be api, not a_p_i
            ("HTMLParser", "html_parser"),                # Should be html, not h_t_m_l
            ("JSONData", "json_data"),                    # Should be json, not j_s_o_n
            ("HTTPSConnection", "https_connection"),      # Should be https, not h_t_t_p_s
            ("URLPath", "url_path"),                      # Should be url, not u_r_l
            ("UserID", "user_id"),                        # Should be user_id, not user_i_d
            ("SimpleCase", "simple_case"),                # Regular camelCase should still work
            ("already_snake", "already_snake"),           # Snake case should be unchanged
        ],
    )
    def test_camel_to_snake_conversion(self, input_str: str, expected: str):
        """Test that camel_to_snake converts strings correctly."""
        result = camel_to_snake(input_str)
        assert result == expected, f"Expected {input_str} -> {expected}, got {result}"

    def test_snake_case_unchanged(self):
        """Test that strings already in snake_case are not modified."""
        snake_cases = [
            "already_snake_case",
            "simple_test",
            "lowercase_with_underscores",
        ]
        for case in snake_cases:
            result = camel_to_snake(case)
            assert result == case, f"Snake case {case} should remain unchanged, got {result}"

    def test_acronym_improvements(self):
        """Test that common acronyms are handled better than before."""
        # These should NOT be split into individual letters
        test_cases = [
            ("XMLParser", "xml_parser"),
            ("HTTPClient", "http_client"), 
            ("JSONSerializer", "json_serializer"),
            ("HTMLRenderer", "html_renderer"),
        ]
        
        for input_str, expected in test_cases:
            result = camel_to_snake(input_str)
            assert result == expected, f"Expected {input_str} -> {expected}, got {result}"
            # Ensure we're not getting individual letter splits
            assert "x_m_l" not in result
            assert "h_t_t_p" not in result
            assert "j_s_o_n" not in result
            assert "h_t_m_l" not in result